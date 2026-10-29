# Plantilla de las páginas del Manual NuHub. Cada plugin es un diccionario (ver datos_*.py).
import html
from diagrama import svg

FUENTES = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
           '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
           '&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">')


def pagina(d):
    flujo = ''.join(
        (f'<span class="{"aqui" if c.get("aqui") else ""}">{c["t"]}</span>' if 'flecha' not in c else f'<em>{c["flecha"]}</em>')
        for c in d['encaja'])
    ficha = ''.join(f'<div><b>{k}</b>{v}</div>' for k, v in d['ficha'])
    diagrama, numeros = svg(d['flujo'], d['aria'])
    pasos = ''.join(
        f'<div class="paso{" decision" if p.get("destacar") else ""}"><div><h3>{p["t"]}</h3>{p["html"]}'
        + (f'<span class="uso">{p["uso"]}</span>' if p.get('uso') else '') + '</div></div>'
        for p in d['pasos'])
    ejemplos = ''.join(
        f'<article class="ejemplo"><h3>{e["t"]}</h3><p class="quien">{e["quien"]}</p><ol>'
        + ''.join(f'<li>{x}</li>' for x in e['pasos'])
        + f'</ol><p class="resultado"><b>Resultado:</b> {e["resultado"]}</p></article>'
        for e in d['ejemplos'])
    tabla = (f'<section><h2>{d["tabla"]["t"]}</h2><p class="bajada">{d["tabla"]["bajada"]}</p><div class="tabla"><table>'
             f'<thead><tr>{"".join(f"<th>{c}</th>" for c in d["tabla"]["cols"])}</tr></thead><tbody>'
             + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in fila) + '</tr>' for fila in d['tabla']['filas'])
             + '</tbody></table></div></section>')
    preguntas = ('<section><h2>Preguntas frecuentes</h2><div class="preguntas">'
                 + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in d['preguntas'])
                 + '</div></section>')
    leyenda_uso = ('<span><span class="paso-uso">1 uso</span> Gasta un uso de la licencia</span>' if d.get('gasta', True)
                   else '')
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{d["nombre"]} · Manual NuHub</title>
<meta name="description" content="{html.escape(d["descripcion"])}">
{FUENTES}
<link rel="stylesheet" href="../estilos.css">
</head>
<body>
<div class="barra">
  <a class="marca" href="../"><i>N</i>Manual NuHub</a>
  <a class="volver" href="../">← Todos los plugins</a>
</div>
<main>
  <div class="arriba">
  <header>
    <div class="panel">{d["panel"]} · {d["nombre"]}</div>
    <h1>{d["titulo"]}</h1>
    <p class="entrada">{d["entrada"]}</p>
  </header>
  <section class="encaja">
    <h2>Dónde encaja</h2>
    <p class="bajada">{d["encaja_texto"]}</p>
    <div class="flujo">{flujo}</div>
  </section>
  </div>

  <section class="ficha" aria-label="Ficha rápida">{ficha}</section>

  <section>
    <h2>Mapa del proceso</h2>
    <p class="bajada">De un vistazo: el recorrido{", las decisiones" if any(i["tipo"] == "rombo" for i in d["flujo"]) else ""} y dónde se gasta la licencia. Los números son los mismos del paso a paso de abajo.</p>
    <div class="diagrama">{diagrama}</div>
    <div class="leyenda-f">
      <span><i></i> Siguiente paso</span><span><i class="si"></i> Sí</span><span><i class="no"></i> No</span>
      <span><b class="r"></b> Decisión</span>{leyenda_uso}
    </div>
  </section>

  <section>
    <h2>Paso a paso</h2>
    <p class="bajada">El detalle de cada paso del mapa: qué botón pulsar y qué pasa.</p>
    <div class="proceso">{pasos}</div>
  </section>

  <section>
    <h2>Ejemplos de uso</h2>
    <p class="bajada">Situaciones reales de un proyecto y cómo se resuelven con {d["nombre"]}.</p>
    <div class="ejemplos">{ejemplos}</div>
  </section>

  <div class="dos">
  {tabla}
  {preguntas}
  </div>
</main>
<footer>© 2026 NuHub · Manual de usuario · {d["nombre"]} {d["version"]} · Los plugins NuHub y su desarrollo son propiedad de NuHub. Para soporte, usa la pestaña PQR del plugin Cuenta NuHub.</footer>
</body>
</html>
'''


def B(t):
    """Nombre de un botón o control del plugin."""
    return f'<span class="boton">{t}</span>'
