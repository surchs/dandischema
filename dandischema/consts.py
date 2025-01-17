DANDI_SCHEMA_VERSION = "0.5.1"
ALLOWED_INPUT_SCHEMAS = ["0.3.0", "0.3.1", "0.4.0", "0.4.1", "0.4.2", "0.4.3", "0.4.4"]

# ATM we allow only for a single target version which is current
# migrate has a guard now for this since it cannot migrate to anything but current
# version
ALLOWED_TARGET_SCHEMAS = [DANDI_SCHEMA_VERSION]
# This allows multiple schemas for validation, whereas target schemas focus on
# migration.
ALLOWED_VALIDATION_SCHEMAS = ALLOWED_TARGET_SCHEMAS + ["0.4.4"]

if DANDI_SCHEMA_VERSION not in ALLOWED_INPUT_SCHEMAS:
    ALLOWED_INPUT_SCHEMAS.append(DANDI_SCHEMA_VERSION)
