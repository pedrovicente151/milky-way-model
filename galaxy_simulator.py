import tkinter as tk
from random import randint, uniform, random
import math
# =============================================================================
SCALE = 225  # Earth's radio bubble
NUM_CIVS = 15600000

root = tk.Tk()
root.title("Milky Way Galaxy")
c = tk.Canvas(root, width=1000, height=1000, bg='black')
c.grid()
c.configure(scrollregion=(-500, -400, 500, 400))

# Milky Way Dimensions
# Fix Code Desgin!!! (Send to Top)
DISC_RADIUS = 50000
DISC_HEIGHT = 1000
DISC_VOL = math.pi * DISC_RADIUS**2 * DISC_HEIGHT


def scale_galaxy():
    """Scale galaxy dimensions based on radio bubble size (scale)
    """
    disc_radius_scaled = round(DISC_RADIUS / SCALE)
    bubble_vol = 4/3 * math.pi * (SCALE / 2)**3
    disc_vol_scaled = DISC_VOL/bubble_vol
    return disc_radius_scaled, disc_vol_scaled


def detect_prob(disc_vol_scaled):
    """Calculate probability of galactic civilizations detecting each other.
    """
    ratio = NUM_CIVS / disc_vol_scaled  # ratio of civs to scaled galaxy volume
    if ratio < 0.002:
        detect_prob = 0
    elif ratio >= 5:
        detect_prob = 1
    else:
        detect_prob = -0.004757 * ratio**4 + 0.06681 * ratio **3 - 0.3605 * \
                      ratio**2 + 0.9215 * ratio + 0.00826
    return round(detect_prob, 3)


def random_polar_coordinates(disc_radius_scaled):
    """Generate uniform random (x, y) point within a disc for 2D display.
    """
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * disc_radius_scaled)
    y = round(math.sqrt(r) * math.sin(theta) * disc_radius_scaled)
    return x, y


def spirals(b, r, rot_fac, fuz_fac, arm):
    """Build spiral arms for tkinter display using logarithmic spiral formula.

    b: arbitrary constant in log spiral equation
    r: scaled galactic disc radius
    rot_fac: rotation factor
    fuz_fac: random shift in star position in arm, applied to 'fuzz' variable
    arm: spiral arm (0 = main arm, 1 = trailing stars
    """
    spiral_starts = []
    fuzz = int((0.030 * abs(r)))  # Random shift start locations
    theta_max_degrees = 520
    for i in range(theta_max_degrees):
        theta = math.radians(i)
        x = r * math.exp(b * theta) * math.cos(theta + math.pi + rot_fac) \
            + randint(-fuzz, fuzz) * fuz_fac
        y = r * math.exp(b * theta) * math.sin(theta + math.pi + rot_fac) \
            + randint(-fuzz, fuzz) * fuz_fac

        spiral_starts.append((x, y))

    for x, y in spiral_starts:
        if arm == 0 and int(x % 2) == 0:
            c.create_oval(x-2, y-2, x+2, y+2, fill='white', outline='')
        elif arm == 0 and int(x % 2) != 0:
            c.create_oval(x-1, y-1, x+1, y+1, fill='white', outline='')
        elif arm == 1:
            c.create_oval(x, y, x, y, fill='white', outline='')


def star_haze(disc_radius_scaled, density):
    """Randomly distribute faint tkinter starts in galactic disc.

    disc_radius = galactic disc radius scaled to radio bubble diameters
    density = multipllier to vary number of starts posted
    """
    for i in range(0, disc_radius_scaled * density):
        x, y = random_polar_coordinates(disc_radius_scaled)
        c.create_text(x, y, fill="white", font=('Helvetica', 7), text='.')

def main():
    """Calculate detection probability & post galaxy display & stats.
    """
    disc_radius_scaled, disc_vol_scaled =  scale_galaxy()
    detection_prob = detect_prob(disc_vol_scaled)

    # build 4 main spiral arms & 4 trailing arms
    spirals(-0.3, disc_radius_scaled, 2, 1.5, 0)
    spirals(-0.3, disc_radius_scaled, 1.91, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, 2, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, -2.09, 1.5, 1)
    spirals(-0.3, -disc_radius_scaled, 0.5, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, 0.4, 1.5, 1)
    spirals(-0.3, -disc_radius_scaled, -0.5, 1.5, 0)
    spirals(-0.3, -disc_radius_scaled, -0.6, 1.5, 1)
    star_haze(disc_radius_scaled, 8)

    c.create_text(-455, -360, fill='white', anchor='w',
                  text='One Pixel = {} LY'.format(SCALE))
    c.create_text(-455, -330, fill='white', anchor='w',
                  text='Radio Bubble Diameter = {} LY'.format(SCALE))
    c.create_text(-455, -300, fill='white', anchor='w',
                  text='Probability of detection for {:,} civilizations = {}'.
                  format(NUM_CIVS, detection_prob))

    if SCALE == 225:
        c.create_rectangle(115, 75, 116, 76, fill='red', outline='')
        c.create_text(118, 72, fill='red', anchor='w',
                      text="<---------- Earth's Radio Bubble")

    root.mainloop()

if __name__ == '__main__':
    main()
