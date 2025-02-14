def shfaq_menu():
    print("\n Menaxhimi i Detyrave")
    print("1. Shto një detyrë")
    print("2. Shfaq detyrat")
    print("3. Fshi një detyrë")
    print("4. Shëno një detyrë si të kryer")
    print("5. Dil")

detyrat = []

while True:
    shfaq_menu()
    zgjedhja = input("Zgjidh një opsion: ")

    if zgjedhja == "1":
        detyra = input(" Shkruaj detyrën: ")
        detyrat.append({"tekst": detyra, "kryer": False})
        print(" Detyra u shtua me sukses!")

    elif zgjedhja == "2":
        print("\n Lista e Detyrave:")
        if not detyrat:
            print("🔹 Nuk ka asnjë detyrë të regjistruar.")
        else:
            for i, detyra in enumerate(detyrat, 1):
                status = "✔" if detyra["kryer"] else ""
                print(f"{i}. {status} {detyra['tekst']}")

    elif zgjedhja == "3":
        if not detyrat:
            print(" Nuk ka detyra për të fshirë!")
        else:
            nr = int(input("🗑 Shkruaj numrin e detyrës për ta fshirë: ")) - 1
            if 0 <= nr < len(detyrat):
                e_fshir = detyrat.pop(nr)
                print(f" Detyra '{e_fshir['tekst']}' u fshi me sukses!")
            else:
                print("⚠ Numri i pavlefshëm! Provo përsëri.")

    elif zgjedhja == "4":
        if not detyrat:
            print(" Nuk ka detyra për të shënuar si të kryera!")
        else:
            nr = int(input("✔ Shkruaj numrin e detyrës për ta shënuar si të kryer: ")) - 1
            if 0 <= nr < len(detyrat):
                detyrat[nr]["kryer"] = True
                print(f" Detyra '{detyrat[nr]['tekst']}' u shënua si e kryer!")
            else:
                print("⚠ Numri i pavlefshëm! Provo përsëri.")

    elif zgjedhja == "5":
        print(" Dalje nga programi...")
        break

    else:
        print("Opsion i pavlefshëm! Provo përsëri.")
