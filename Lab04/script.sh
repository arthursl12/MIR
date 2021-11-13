
LAB=lab04

echo "Baixando os arquivos do lab. Pode demorar um pouco."
if [ -f files.zip ]; then rm files.zip; fi
wget -q --no-check-certificate --show-progress         https://dcc.ufmg.br/~flaviovdf/mir/$LAB/files.zip
echo

if [ -f files.zip ]; then
    echo "Extraindo..."
    unzip -o files.zip
    if ! [ $? -eq 0 ]; then
        echo "Erro extraindo o arquivo!"
    fi
else
    echo "Arquivo não baixado!"
fi
