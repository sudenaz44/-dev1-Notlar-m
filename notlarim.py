def sinav_calisma_programi():
    konular = ["Git nedir", "Commit nasıl atılır", "Branch ne işe yarar", "Merge çatışması nedir"]
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe"]

    program = {}

    for i in range(len(konular)):
        if i < len(gunler):
            program[gunler[i]] = konular[i]
        else:
            program["Ekstra Gün"] = konular[i]

    for gun, konu in program.items():
        print(f"{gun} günü şu çalışılacak: {konu}")

sinav_calisma_programi()
