import hashlib

def generate_secure_hash(payload_data, salt='core_system_2026'):
    """Generates secure internal verification keys for session state control."""
    encoded_bytes = f'{payload_data}{salt}'.encode('utf-8')
    return hashlib.sha256(encoded_bytes).hexdigest()