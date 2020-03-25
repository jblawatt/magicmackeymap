"""
python module to map windows key to
mac magic keyboard. switch windows and alt
and the <|> with ^°.

and all i see in the meantime

TODO:
    - right option mapping has an error. should map to right windows.
        but maps to alt. don't know why.
    - why does remapped keys not trigger the on_pres event?

"""
import keyboard
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help="log every unmapped key")
parser.add_argument('-n', '--nomap', dest='nomap', action='store_true', help='just use it as debuggung!! keylogger')


keys = (
    (41, 86),
    (86, 41),

    ('rechte windows', 541),
    (541, 'rechte windows'),

    (91, 'alt'),
    (56, 'linke windows'),
)



def on_key_press(e: keyboard.KeyboardEvent):
    print(
        "KeyPressEvent: name=%s scan_code=%s time=%s." %
            ( e.name
            , e.scan_code
            , e.time
            ),
        )


def main():
    args = parser.parse_args()
    if args.verbose:
        keyboard.on_press(on_key_press)

    if not args.nomap:
        for mapit in keys:
            keyboard.remap_key(*mapit)

    print("mac mode is activated now, my little apple fanboy... ;-)")

    keyboard.wait()



if __name__ == '__main__':
    main()
