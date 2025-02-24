from ninja import Router, Query
from .schemas import LivrosSchema, AvaliacaoSchema, FiltrosSortear
from .models import Livros, Categorias


livros_router = Router()

@livros_router.post('/')
def creater_livros(request, livro_schema: LivrosSchema):
    nome = livro_schema.dict()['nome']
    streaming = livro_schema.dict()['streaming']
    categorias= livro_schema.dict()['categoria']
    
    if streaming not in ['F', 'AK']:
        return 400,{'status': 'Erro: streaming deve ser F ou K'}
    
    livro = Livros(
        nome = nome,
        streaming = streaming,
    )
    livro.save()

    

    for categoria in categorias:
        categoria_temp = Categorias.objects.get(id=categoria)
        livro.categorias.add(categoria_temp) 

    return {'status':'ok'}


@livros_router.put('/{livro_id}')
def avaliar_livro(request, livro_id : int, avaliacao_schema: AvaliacaoSchema):
    comentarios = avaliacao_schema.dict()['comentarios']
    nota = avaliacao_schema.dict()['nota']
    if nota < 0 or nota >5:
        return 400, {'Status' : 'Error: Nota deve ser entre 0 a 5'}
    try:
        livro = Livros.objects.get(id= livro_id)
        livro.comentarios = comentarios
        livro.nota = nota
        livro.save()

        return 200, {'status': 'Avaliação realizada com sucesso'}
    except:
        return 500, {'status': 'Erro interno do servidor'}


@livros_router.delete('/{livro_id}')
def deletar_livro(request, livro_id: int):
    livro = Livros.objects.get(id= livro_id)
    livro.delete()

    return livro_id  
    
@livros_router.get('/sortear/', response={200: LivrosSchema, 404:dict})
def sortear_livro(request, filtros: Query[FiltrosSortear]):
    nota_minima = filtros.dict()['nota_minima']
    categoria = filtros.dict()['categorias']
    reler = filtros.dict()['reler']

    livros = Livros.objects.all()
    if not reler:
        livros = livros.filter(nota = None)
    if nota_minima:
        livros = livros.filter(nota__gte=nota_minima)

    if categoria:
        livros= livros.filter(categorias__id=categoria)     

    livro = livros.order_by('?')       

    if livros.count() > 0:
        return 200, livro


    return {'ok':'ok'}    

