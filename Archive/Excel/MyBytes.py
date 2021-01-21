import io

stream_str = io.BytesIO(b"JournalDev Python: \x00\x01")
print(stream_str.getvalue())
