def anamnese(): 
    sexo = int(input("Informe o seu sexo? (1)Feminino , (2)Masculino\n"))
    idade = int(input("Informe sua idade?\n"))
    altura = float(input("Informe a sua altura?\n"))
    peso = float(input("Informe o seu peso?\n"))
    tipo_diabetes = input("Informe o tipo da sua Diabetes: Tipo I (1) , Tipo II (2) , Gestacional (3) , MODY (4) , LADA (5), Outro (6)\n")
    terapia = input("Qual é a sua terapia? Medicamento sem insulina (1), Injeções diárias (2), Bomba de insulina (3), Outra terapia (4), Não faço uso de terapia (5)\n")
    if terapia == 1:
        input("Qual o medicamento que você usa?\n")
        input("Qual a dosagem desse medicamento?\n")
    elif terapia == 2:
        input("Qual o aumento da dose de insulina na caneta? 0.5U , 1U , 2U\n")
    elif terapia == 3:
        input("Qual a marca da Bomba de insulina?\n")
    elif terapia == 4:
        input("Informe qual outra terapia você utiliza?\n")
    else:
        print("Usuário não faz uso de terapia.")

    #Obs)1) Existem 31 medicamentos diferentes, alguns com dosagem única, mas a maioria com diferentes dosagens.
    #Obs)2) Existem 8 marcas diferentes de bomba de insulina.
    
    unidades_medida = input("Especifique as unidades de medida: US (lbs, oz, fl oz, inch) , Métrico (Kg, g, mL, cm)")
    unidade_glicemia = input("Qual a unidade que você mede sua glicemia? mg/mL , mmol/L")

    # Metas Glicêmicas personalizadas pelo usuário
    hipoglicemia = int(input("Informe qual é seu nível de hipoglicemia?\n"))
    glicemia_baixa = int(input("Informe qual é seu nível de glicemia baixa?\n"))
    glicemia_desejada = int(input("Informe qual é seu nível de glicemia desejada?\n"))
    glicemia_alta = int(input("Informe qual é seu nível glicemia alta?\n"))
    hiperglicemia = int(input("Informe qual é seu nível de hiperglicemia?\n"))

