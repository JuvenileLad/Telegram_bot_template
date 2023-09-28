def exec(e):
    source = e.__traceback__.tb_frame.f_code.co_filename
    source = source.split("/")[-1]
    lineN = e.__traceback__.tb_lineno
    eType = type(e).__name__
    ex = e
    print(f"ERROR:\n{source} : {lineN}\n{eType} : {e}")
    ErrLog = f"**#Error**\n`{source}` **|** `{lineN}`\n**{eType}** : `{e}`"
    return ErrLog