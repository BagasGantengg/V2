import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
