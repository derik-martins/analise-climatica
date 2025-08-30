import csv 
import matplotlib.pyplot as plt

MESES_DIC = {
    1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
    7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'
}

def carregar_dados(nome_arquivo):
    dados_climaticos = []
    try:
        with open(nome_arquivo, mode = 'r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            for linha in leitor_csv:
                try:
                    dados_processados = {
                        'data': linha['data'],
                        'precip': float(linha['precip']),
                        'maxima': float(linha['maxima']),
                        'minima': float(linha['minima']),
                        'horas_insol': float(linha['horas_insol']),
                        'temp_media': float(linha['temp_media']),
                        'um_relativa': float(linha['um_relativa']),
                        'vel_vento': float(linha['vel_vento'])
                    }

                    dados_climaticos.append(dados_processados)
                except (ValueError, TypeError):
                    continue
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado!, Tente denovo!")
    return dados_climaticos

def visualizar_dados_periodo(dados):
    print("\n--- Visualização de Dados por Período ---")
    try:
        mes_inicio = int(input("Digite o mês inicial (1-12): "))
        ano_inicio = int(input("Digite o ano inicial (ex: 1980): "))
        mes_fim = int(input("Digite o mês final (1-12): "))
        ano_fim = int(input("Digite o ano final (ex: 2016): "))

        if not (1 <= mes_inicio <= 12 and 1 <= mes_fim <= 12):
            print("ERRO: Mês inválido")
            return
        
        print("\nQual Conjunto de Dados Você Deseja Visualizar?")
        print("1) Todos os dados")
        print("2) Apenas precipitação")
        print("3) Apenas temperaturas (Minima e Máximo)")
        print("4) Apenas umidade e vento")
        escolha = input("Escolha uma opção (1-4): ")
        
        dados_filtrados = []
        for registro in dados:
            dia_registro, mes_registro, ano_registro = map(int, registro['data'].split('/'))
            if (ano_registro > ano_inicio or (ano_registro == ano_inicio and mes_registro >= mes_inicio)) and \
                (ano_registro < ano_fim or (ano_registro == ano_fim and mes_registro <= mes_fim)):
                dados_filtrados.append(registro)

        if not dados_filtrados:
            print("\n Nenhum dado encontrado para este periodo")
            return
        
        elif escolha == '1':
            print("\n{:<12} {:<12} {:<10} {:<10} {:<10} {:<10}".format(
                'Data', 'Precip(mm2)', 'Max(C°)', 'Min(C°)', 'Umidade(%)', 'Vento (m/s)'))
            print("-" * 70)
            for r in dados_filtrados:
                print("{:<12} {:<12.1f} {:<10.1f} {:<10.1f} {:<10.1f} {:<10.1f}".format(
                    r['data'], r['precip'], r['maxima'], r['minima'], r['um_relativa'], r['vel_vento']
                ))

        elif escolha == '2':
            print("\n{:<12} {:<12}".format('Data', 'Precip (mm²)'))
            print("-" * 25)
            for r in dados_filtrados:
                print("{:<12} {:<12.1f}".format(r['data'], r['precip']))

        elif escolha == '3':
            print("\n{:<12} {:<10} {:<10}".format('Data', 'Max(°C)', 'Min(°C)'))
            print("-" * 35)
            for r in dados_filtrados:
                print("{:<12} {:<10.1f} {:<10.1f}".format(r['data'], r['maxima'], r['minima']))
        
        elif escolha == '4':
            print("\n{:<12} {:<12} {:<12}".format('Data', 'Umidade (%)', 'Vento (m/s)'))
            print("-" * 40)
            for r in dados_filtrados:
                print("{:<12} {:<12.1f} {:<12.1f}".format(r['data'], r['um_relativa'], r['vel_vento']))
        else:
            print("ERRO: Opção de Visualização Inválida")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números inteiros para meses e anos.")

def encontrar_mes_mais_chuvosa(dados):
    print("\n--- Mês Mais Chuvoso (1961-2016) ---")
    precipitacao_mensal = {}

    for registro in dados:
        dia, mes, ano = registro['data'].split('/')
        chave = f"{int(mes):02d}/{ano}"

        precipitacao_mensal[chave] = precipitacao_mensal.get(chave, 0) + registro['precip']

    if not precipitacao_mensal:
        print("Não Foi possivel calcular, não há dados de precipitação")
        return
    
    mes_mais_chuvoso = max(precipitacao_mensal, key=precipitacao_mensal.get)
    maior_precipitacao = precipitacao_mensal[mes_mais_chuvoso]

    mes_num, ano_num = map(int, mes_mais_chuvoso.split('/'))

    print(f"O mês com maior volume de chuva foi {MESES_DIC[mes_num]}/{ano_num}.")
    print(f"Volume total de precipitação: {maior_precipitacao:.2f} mm")

def calcular_media_temp_minima_mes(dados):
    print("\n--- Média de Temperatura Minima por Mês (1961 - 2016)---")
    try:
        mes_usuario = int(input("Digite o mês para análise (1-12): "))
        if not (1 <= mes_usuario <= 12):
            print("Erro: Mês inválido. Por favor, insira um valor entre 1 e 12.")
            return None
        
        nome_mes = MESES_DIC[mes_usuario]
        medias_anuais = {}

        for ano in range(2006, 2017):
            temperaturas_mes = []
            for registro in dados:
                dia_reg, mes_reg, ano_reg = map(int, registro['data'].split('/'))
                if ano_reg == ano and mes_reg == mes_usuario:
                    temperaturas_mes.append(registro['minima'])
            
            if temperaturas_mes:
                media = sum(temperaturas_mes) / len(temperaturas_mes)
                chave = f"{nome_mes}{ano}"
                medias_anuais[chave] = media

        print(f"\nMédias da temperatura minima para {nome_mes} (2006 - 2016): ")
        for chave, valor in medias_anuais.items():
            print(f"- {chave}: {valor:.2f}C")

        return medias_anuais, nome_mes
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
        return None
    
def gerar_grafico_barras(dados_medias, nome_mes):
    if not dados_medias:
        print("Não há dados para gerar os gráficos. Exexcute a opção 'c primeiro'.")
        return
    
    anos = list(dados_medias.keys())
    medias = list(dados_medias.values())

    plt.figure(figsize=(12, 7))
    bars = plt.bar(anos, medias, color='skyblue')

    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Temperatura Mínima Média C°', fontsize=12)
    plt.title(f'Média da Temperatura Mínima em {nome_mes} (2006 - 2016)', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center')
    print("\nExibindo o gráfico de barras. Feche a janela do gráfico para continuar.")
    plt.show()

def calcular_media_geral_periodo(dados_medias, nome_mes):
    if not dados_medias:
        print("Não há dados para gerar os gráficos. Exexcute a opção 'c primeiro'.")
        return
    
    media_geral = sum(dados_medias.values()) / len(dados_medias.values())

    print(f"\n--- Média geral para {nome_mes} (2006 - 2016) ---")
    print(f"A média geral da temperatura mínima para o mês de {nome_mes} nos ultimos 11 anos foi de {media_geral:.2f}C")

def main():
    nome_do_arquivo = 'analisar.csv'
    dados = carregar_dados(nome_do_arquivo)

    if not dados:
        print("Finalizando o programa devido a falta de dados!!")
        return
    print(f"Carga de dados concluída {len(dados)} registros válidos foram carregados!!")

    dados_media_temp_minima = None
    nome_mes_analisado = ""

    while True:
        print("\n--- Análise Climática de Porto Alegre (1961 - 2016)")
        print("a) Visualizar dados por período")
        print("b) Encontrar o mês mais chuvoso")
        print("c) Calcular médias de temperatura mínima para um mês (2006 - 2016)")
        print("d) Gerar gráfico das médias de temperatura mínima (requer 'c')")
        print("e) Calcular média geral da temperatura mínima para o mês (requer 'c')")
        print("s) Sair")

        opcao = input("\nEscolha uma opção: ").lower()

        if opcao == 'a':
            visualizar_dados_periodo(dados)
        elif opcao == 'b':
            encontrar_mes_mais_chuvosa(dados)
        elif opcao == 'c':
            resultado = calcular_media_temp_minima_mes(dados)
            if resultado:
                dados_media_temp_minima, nome_mes_analisado = resultado
        elif opcao == 'd':
            if dados_media_temp_minima:
                gerar_grafico_barras(dados_media_temp_minima, nome_mes_analisado)
            else:
                print("ERRO: É necessário executar a opção 'c' primeiro para gerar os dados do gráfico.")
        elif opcao == 'e':
            if dados_media_temp_minima:
                calcular_media_geral_periodo(dados_media_temp_minima, nome_mes_analisado)
            else:
                print("ERRO: É necessário executar a opção 'c' primeiro para gerar os dados para o cálculo.")
        elif opcao == 's':
            print("Finalizando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
        
if __name__ == "__main__":
    main()