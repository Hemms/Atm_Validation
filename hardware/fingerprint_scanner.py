from pyfingerprint.pyfingerprint import PyFingerprint

def capture_fingerprint():
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    if f.verifyPassword() == False:
        raise ValueError('Fingerprint sensor password is incorrect!')

    print('Waiting for finger...')
    while f.readImage() == False:
        pass

    f.convertImage(0x01)
    return f.downloadCharacteristics(0x01)

def verify_fingerprint(stored_template, scanned_template):
    return stored_template == scanned_template  # Simple comparison, improve as needed
