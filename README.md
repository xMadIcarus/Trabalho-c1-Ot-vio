# Trabalho-c1-Otavio
Classificação de Resíduos com Inteligência Artificial
Descrição
Este projeto é uma aplicação web que utiliza Inteligência Artificial e Visão Computacional para o reconhecimento de imagens de resíduos recicláveis. O objetivo 
principal é realizar uma classificação binária focada em distinguir duas categorias específicas: Metal e Vidro Verde (Green Glass).  Tecnologias UtilizadasFront-end: 
Construído de forma nativa com HTML5, CSS3 (com Flexbox) e JavaScript (Vanilla).  Inteligência Artificial: O modelo foi treinado no Google Teachable Machine e 
integrado à aplicação web através da biblioteca TensorFlow.js.  Avaliação: Script em Python utilizando TensorFlow e Scikit-Learn.  Dataset e DesempenhoBase de Dados: 
Foi utilizado o dataset "Garbage Classification" disponível no Kaggle.  Arquitetura: O projeto utiliza o modelo base MobileNetV2, ideal para processamento local no 
navegador (Edge Computing).  Métricas: Aplicando o Princípio de Pareto (80% treino / 20% teste), o modelo obteve 100% de Acurácia, Precisão, Recall e F1-Score, sem 
registrar Falsos Positivos ou Falsos Negativos na Matriz de Confusão.  Como Executar o Projeto LocalmenteDevido às políticas de segurança dos navegadores (CORS) ao 
carregar arquivos locais como o modelo de IA (model.json e weights.bin), o projeto não deve ser aberto apenas com um duplo clique no arquivo HTML. É necessário um 
servidor web local.  Faça o download ou clone este repositório no seu computador.Abra a pasta do projeto em um editor de código, como o Visual Studio Code (VS Code).  
Instale a extensão Live Server no seu VS Code.  Clique com o botão direito no arquivo index.html e selecione "Open with Live Server".O seu navegador padrão abrirá a 
interface automaticamente. A partir daí, você pode testar a classificação via Webcam ou fazendo o upload de uma imagem.
