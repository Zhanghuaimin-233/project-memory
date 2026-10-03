"""Offline batch implementation; the injected gateway owns external effects."""

BATCH_SIZE = 10


def import_records(records, gateway, store):
    for offset in range(0, len(records), BATCH_SIZE):
        batch = records[offset:offset + BATCH_SIZE]
        result = gateway.send_batch(batch)
        store.append(result)
    return len(store)
