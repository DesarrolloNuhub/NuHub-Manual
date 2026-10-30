# Genera las páginas del Manual NuHub: python3 _generador/generar.py (desde la raíz del repositorio)
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pagina import pagina, FUENTES
import datos_calidad, datos_gestion

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
todas = datos_calidad.PAGINAS + datos_gestion.PAGINAS
for d in todas:
    os.makedirs(os.path.join(RAIZ, d['carpeta']), exist_ok=True)
    open(os.path.join(RAIZ, d['carpeta'], 'index.html'), 'w', encoding='utf-8').write(pagina(d))
    print('ok', d['carpeta'])

por = {d['carpeta']: d for d in todas}
GRUPOS = [('Calidad BIM', ['auditor', 'cantidades', 'matriz-loin']),
          ('Gestión BIM', ['colisiones', 'revisor', 'editar-informacion', 'renombrar', 'plantillas', 'parametros', 'exportadores']),
          ('Externos', ['validador', 'externos']),
          ('Tu cuenta', ['cuenta'])]
RESUMEN = {'auditor': 'Audita el modelo con las reglas del BEP.', 'cantidades': 'Cantidades del modelo a Excel y PDF.',
           'matriz-loin': 'Revisa la información que exige el proyecto por elemento.', 'colisiones': 'Detecta y sigue interferencias entre disciplinas.',
           'revisor': 'Lleva los «No cumple» del Auditor al modelo y sigue las correcciones.', 'editar-informacion': 'Edita parámetros de muchos elementos a la vez.',
           'renombrar': 'Renombra familias, tipos, vistas, CAD y worksets.', 'plantillas': 'Ordena, compara, copia y asigna plantillas de vista.',
           'parametros': 'Crea parámetros y limpia duplicados.', 'exportadores': 'Exporta planos, vistas y tablas por lotes.',
           'validador': 'Compara entregas: auditoría, cantidades, LOIN y colisiones.', 'externos': 'Procesa hasta 30 modelos por lote, también planos en PDF y DWG.',
           'cuenta': 'Tu cuenta, plan, usos, actualizaciones y PQR a soporte.'}
secciones = ''.join(
    f'<section class="grupo"><h2>{g}</h2><div class="tarjetas">'
    + ''.join(f'<a class="tarjeta" href="{c}/"><b>{por[c]["nombre"]}</b><span>{RESUMEN[c]}</span></a>' for c in cs)
    + '</div></section>' for g, cs in GRUPOS)
indice = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Manual NuHub</title>
<meta name="description" content="Manual de usuario de los plugins NuHub para Autodesk Revit: qué hace cada plugin, el mapa de su proceso y ejemplos de uso.">
{FUENTES}
<link rel="stylesheet" href="estilos.css">
</head>
<body>
<div class="barra"><a class="marca" href="./"><i>N</i>Manual NuHub</a></div>
<main>
  <header>
    <div class="panel">Plugins para Autodesk Revit 2024 · 2025 · 2026</div>
    <h1>Manual de los plugins NuHub</h1>
    <p class="entrada">Qué hace cada plugin, el mapa de su proceso paso a paso y ejemplos de uso en un proyecto real. Todos están en la pestaña <b>NuHub</b> de Revit y funcionan con una sola cuenta NuHub.</p>
  </header>
  {secciones}
</main>
<footer>© 2026 NuHub · nuhub.com.co · Los plugins NuHub y su desarrollo son propiedad de NuHub. Para soporte, usa la pestaña PQR del plugin Cuenta NuHub.</footer>
</body>
</html>
'''
open(os.path.join(RAIZ, 'index.html'), 'w', encoding='utf-8').write(indice)
print('ok index')
