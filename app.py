from flask import Flask, render_template

app = Flask(__name__)

from books import Book
book1 = Book()
book1.set_id(1)
book1.set_title('Harry Potter')
book1.set_year(1997)
book1.set_img('harry_potter.jpg')
book1.set_author('J.K Rowling')
book1.set_genre('Fantasia')
book1.set_about('Harry Potter, um garoto órfão criado pelos tios, descobre no seu 11º aniversário que é um bruxo. Ele é convidado a estudar na Escola de Magia e Bruxaria de Hogwarts, onde faz grandes amizades, especialmente com Rony e Hermione. Lá, Harry aprende sobre seu passado, sua ligação com o poderoso bruxo das trevas Voldemort e enfrenta perigos ao tentar proteger a Pedra Filosofal, um objeto mágico com grande poder. A história marca o início de uma jornada extraordinária.')
book1.set_about_author('J.K. Rowling é uma escritora britânica, mundialmente famosa por criar a série Harry Potter. Nascida em 1965, superou dificuldades financeiras antes do sucesso. Sua obra impactou gerações, vendendo milhões de livros. Além da literatura, atua em causas sociais e escreveu sob o pseudônimo Robert Galbraith.')
book1.set_photo_author('jk_rowling.jpg')

book2 = Book()
book2.set_id(2)
book2.set_title('Percy Jackson')
book2.set_year(2005)
book2.set_img('percy_jackson.jpg')
book2.set_author('Rick Riordan')
book2.set_genre('Fantasia')
book2.set_about('Percy Jackson, um adolescente com dificuldades escolares, descobre ser um semideus, filho de Poseidon. Após ser acusado de roubar o raio-mestre de Zeus, embarca em uma jornada cheia de perigos ao lado dos amigos Grover e Annabeth. Enquanto enfrenta monstros e deuses da mitologia grega, Percy precisa provar sua inocência e evitar uma guerra entre os deuses do Olimpo. A aventura marca o início de sua descoberta sobre identidade, coragem e seu papel no mundo mitológico.')
book2.set_about_author('Rick Riordan é um autor norte-americano, nascido em 1964, conhecido por criar a série Percy Jackson e os Olimpianos. Ex-professor de história, mistura mitologia com aventura juvenil. Seus livros conquistaram leitores no mundo inteiro. Também escreveu séries baseadas nas mitologias egípcia e nórdica, como As Crônicas dos Kane.')
book2.set_photo_author('rick_riordan.png')


book3 = Book()
book3.set_id(3)
book3.set_title('Caraval')
book3.set_year(2017)
book3.set_img('caraval.jpg')
book3.set_author('Stephanie Garber')
book3.set_genre('Romance')
book3.set_about('Scarlett Dragna sempre sonhou em assistir ao Caraval, um espetáculo mágico onde a plateia participa do jogo. Quando finalmente recebe o convite, ela e sua irmã Tella são levadas para um mundo repleto de ilusões e perigos. No entanto, Tella desaparece, e Scarlett precisa vencê-lo para encontrá-la. À medida que o jogo avança, realidade e fantasia se misturam, colocando tudo em risco — inclusive sua sanidade. Caraval é uma jornada encantadora e sombria sobre amor, sacrifício e descobertas')
book3.set_about_author('Stephanie Garber é uma autora norte-americana conhecida pela trilogia Caraval, que mistura fantasia, romance e mistério. Seus livros encantam leitores com mundos mágicos e reviravoltas emocionantes. Ganhou destaque no cenário da literatura jovem adulta contemporânea e continua a expandir seu universo com a série Era Uma Vez um Coração Partido.')
book3.set_photo_author('stephanie_garber.jpg')

book4 = Book()
book4.set_id(4)
book4.set_title('Sherlock Holmes')
book4.set_year(1887)
book4.set_img('sherlock_holmes.jpg')
book4.set_author('Arthur Conan Doyle')
book4.set_genre('Mistério')
book4.set_about('No romance Um Estudo em Vermelho, o brilhante detetive Sherlock Holmes é apresentado ao lado de seu futuro parceiro, Dr. Watson. Juntos, eles investigam um assassinato misterioso em Londres, marcado por pistas intrigantes e uma palavra escrita com sangue na parede: "RACHE". A trama mistura dedução lógica, investigação criminal e flashbacks sobre a motivação do crime. É o primeiro passo na construção da lenda de Holmes, revelando sua genialidade e o início da icônica dupla com Watson')
book4.set_about_author('Arthur Conan Doyle foi um escritor e médico britânico, nascido em 1859. Ganhou fama mundial ao criar o icônico detetive Sherlock Holmes. Suas histórias, cheias de mistério e dedução lógica, marcaram a literatura policial. Também escreveu romances históricos, ficção científica e defendeu o espiritismo até sua morte, em 1930.')
book4.set_photo_author('arthur-conan.jpg')

book5 = Book()
book5.set_id(5)
book5.set_title('O Hobbit')
book5.set_year(1937)
book5.set_img('ohobbit.jpg')
book5.set_author('J.R.R. Tolkien')
book5.set_genre('Ficção')
book5.set_about('Bilbo Bolseiro, um hobbit pacato, é surpreendido ao ser convidado por Gandalf e um grupo de anões para uma aventura rumo à Montanha Solitária. Lá, enfrentarão o dragão Smaug para recuperar um tesouro ancestral. Pelo caminho, Bilbo descobre coragem, enfrenta trolls, aranhas gigantes, elfos e encontra um anel mágico — o mesmo que mais tarde será central em O Senhor dos Anéis. A jornada transforma o tímido hobbit em um herói inesperado, marcando o início de uma das maiores sagas da fantasia.')
book5.set_about_author('J.R.R. Tolkien foi um escritor, linguista e professor britânico, nascido em 1892. É mundialmente conhecido por suas obras de fantasia épica, como O Senhor dos Anéis e O Hobbit. Criou línguas, mitologias e mundos ricos em detalhes. Sua obra influenciou profundamente o gênero fantástico. Faleceu em 1973.')
book5.set_photo_author('jrr_tolkien.jpg')

book6 = Book()
book6.set_id(6)
book6.set_title('Orgulho e Preconceito')
book6.set_year('1813')
book6.set_img('orgulho_preconceito.jpg')
book6.set_author('Jane Austen')
book6.set_genre('Romance')
book6.set_about('Elizabeth Bennet é uma jovem inteligente que vive numa sociedade onde o casamento é prioridade. Quando conhece o reservado e orgulhoso Sr. Darcy, ambos enfrentam seus próprios preconceitos. Entre conflitos sociais e familiares, o romance deles se desenvolve aos poucos, baseado em amadurecimento e compreensão mútua. A obra critica os costumes da época, especialmente a pressão sobre as mulheres. Com diálogos afiados e personagens cativantes, o livro é um dos romances mais importantes da literatura inglesa.')
book6.set_about_author('Jane Austen foi uma escritora britânica do século XIX, conhecida por seus romances que retratam a sociedade inglesa com ironia e crítica social. Suas obras mais famosas, como Orgulho e Preconceito e Razão e Sensibilidade, exploram amor, classe social e costumes, marcando a literatura com personagens femininas fortes e memoráveis.')
book6.set_photo_author('jane-austen.jpg')

book7 = Book()
book7.set_id(7)
book7.set_title('Expresso do Oriente')
book7.set_year('1934')
book7.set_img('agatha_christie.jpg')
book7.set_author('Agatha Christie')
book7.set_genre('Mistério')
book7.set_about('Durante uma viagem a bordo do luxuoso Expresso do Oriente, um passageiro é assassinado durante a noite. Por sorte (ou destino), o detetive Hercule Poirot está no trem e começa a investigar. Todos os passageiros são suspeitos, e o caso se complica quando cada um parece esconder algo. Com inteligência e observação aguçada, Poirot revela uma reviravolta surpreendente. É uma das histórias mais famosas de Agatha Christie, com final icônico e genial, onde nada é o que parece.')
book7.set_about_author('Agatha Christie foi uma escritora britânica, mestre do romance policial, nascida em 1890. Criou personagens icônicos como Hercule Poirot e Miss Marple. Escreveu mais de 80 livros, traduzidos mundialmente. Suas tramas envolventes, cheias de mistério e reviravoltas, fizeram dela a autora mais vendida da história, após Shakespeare e a Bíblia.')
book7.set_photo_author('agatha-christie.jpg')

book8 = Book()
book8.set_id(8)
book8.set_title('Viagem ao Centro da Terra')
book8.set_year(1864)
book8.set_img('julio_verne.jpg')
book8.set_author('Jules Verne')  
book8.set_genre('Ficção')
book8.set_about('O professor Otto Lidenbrock, seu sobrinho Axel e o guia Hans embarcam numa expedição para o centro da Terra, inspirados por um antigo manuscrito. Entrando por um vulcão na Islândia, descobrem um mundo subterrâneo cheio de criaturas pré-históricas, oceanos internos e formações geológicas incríveis. A jornada é repleta de perigos e descobertas que desafiam a lógica da ciência da época. Verne mistura conhecimento científico e imaginação, criando um dos primeiros e mais influentes romances de ficção científica da história.')
book8.set_about_author('Jules Verne foi um escritor francês do século XIX, considerado um dos pais da ficção científica. Suas obras, como Vinte Mil Léguas Submarinas e A Volta ao Mundo em 80 Dias, misturam aventura e ciência. Visionário, antecipou invenções modernas e influenciou gerações com seu espírito explorador e imaginativo.')
book8.set_photo_author('jules_verne.jpg')

book_list = [book1, book2, book3, book4, book5, book6, book7, book8]

@app.route('/')
def home():
    return render_template('home.html', book_list = book_list)

@app.route('/detalhes/<int:id>')
def details(id):
    for book in book_list:
        if book.get_id() == id:
            return render_template('details.html', book = book)
    return 'Autor não encontrado'

#* selecionar os gêneros:
# dicionário generos, onde cada chave é o nome do gênero (fantasia) e o valor é uma lista com os livros pertencentes a aquele gênero
@app.route('/genre')
def genre():
    genre_dict = {}
    for book in book_list:
        genre = book.get_genre()
        
        if genre not in genre_dict:
            genre_dict[genre] = [] #se esse gênero não tiver no dicionário, cria uma lista pra ele
        
        genre_dict[genre].append(book)
    return render_template ('genre.html', genres = genre_dict)

@app.route('/author') #é uma lista de autores
def authors():
    return render_template('author.html', authors = book_list)