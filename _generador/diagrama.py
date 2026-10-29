# Diagrama de flujo con íconos (SVG) para el Manual NuHub.
# Pasos en filas de hasta 5, en zigzag (fila 1 →, fila 2 ←, ...). Rombos = decisiones con rama «No» a una nota
# o de vuelta a un paso anterior (ciclo, dibujado por debajo de la fila).

ICONOS = {
    'abrir':    'M4 5h16v12H4z M4 9h16 M8 21h8 M12 17v4',
    'archivo':  'M7 3h7l4 4v14H7z M14 3v4h4 M10 12h5 M10 15h5 M10 18h3',
    'lista':    'M9 6h11 M9 12h11 M9 18h11 M4 6h1 M4 12h1 M4 18h1',
    'cubo':     'M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5 M12 12v9 M12 12L4 7.5',
    'mira':     'M12 3v4 M12 17v4 M3 12h4 M17 12h4 M12 8a4 4 0 1 0 0.01 0z',
    'check':    'M4 12l5 5L20 6',
    'excel':    'M6 3h12v18H6z M9 8l6 8 M15 8l-6 8',
    'limpiar':  'M4 7h16 M9 7V4h6v3 M6 7l1 13h10l1-13 M10 11v6 M14 11v6',
    'lupa':     'M11 4a7 7 0 1 0 0.01 0z M16 16l5 5',
    'ajustes':  'M4 6h10 M18 6h2 M4 12h4 M12 12h8 M4 18h12 M20 18h0 M14 4v4 M8 10v4 M16 16v4',
    'play':     'M7 4l13 8-13 8z',
    'grafico':  'M4 20V10 M10 20V4 M16 20v-7 M3 20h18',
    'pdf':      'M7 3h7l4 4v14H7z M14 3v4h4 M9 13h2a1.5 1.5 0 0 1 0 3H9v-3z M9 16v2',
    'carpeta':  'M3 6h6l2 2h10v11H3z',
    'lapiz':    'M4 20l4-1 11-11-3-3L5 16z M14 6l3 3',
    'texto':    'M4 6h16 M12 6v13 M8 19h8',
    'capas':    'M12 3l9 5-9 5-9-5z M3 13l9 5 9-5',
    'etiqueta': 'M3 12V4h8l10 10-8 8z M7.5 7.5h0.01',
    'comparar': 'M7 4v16 M17 4v16 M3 8h8 M13 16h8 M9 6l2 2-2 2 M15 14l-2 2 2 2',
    'usuario':  'M8 8a4 4 0 1 0 8 0a4 4 0 1 0 -8 0 M4 21c1-4 4-6 8-6s7 2 8 6',
    'mensaje':  'M4 5h16v11H9l-5 4z M8 9h8 M8 12h5',
    'imagen':   'M4 5h16v14H4z M4 16l5-5 4 4 3-3 4 4 M15 9h0.01',
    'filtro':   'M4 5h16l-6 8v6l-4-2v-4z',
    'lote':     'M6 4h12v4H6z M4 10h16v4H4z M6 16h12v4H6z',
    'enviar':   'M4 12l16-8-6 16-3-6z M11 14l9-10',
    'plantilla':'M4 4h16v16H4z M4 9h16 M9 9v11',
    'colision': 'M9 9a5 5 0 1 0 0.01 0z M15 9a5 5 0 1 0 0.01 0z',
    'llave':    'M8 15a4 4 0 1 1 3-3l9 0 0 3-2 0 0 2-3 0 0-2-4 0',
}

W, H = 176, 128          # tamaño de cada paso
XS = [100, 310, 520, 730, 940]
XG = 1120                # columna del giro entre filas
Y0, DY = 100, 230        # primera fila y separación entre filas


def _nodo(x, y, n, it):
    icono, t1, t2, sub = it['icono'], it['t1'], it.get('t2'), it.get('sub')
    s = f'<g class="nodo" transform="translate({x - W / 2},{y - H / 2})">'
    s += f'<rect width="{W}" height="{H}" rx="12"/>'
    s += f'<circle class="aro" cx="{W / 2}" cy="34" r="24"/>'
    s += f'<g transform="translate({W / 2 - 13.8},{34 - 13.8}) scale(1.15)"><path class="ico" d="{ICONOS[icono]}"/></g>'
    s += f'<circle class="num" cx="22" cy="20" r="11"/><text class="num-t" x="22" y="24.5" text-anchor="middle">{n}</text>'
    s += f'<text class="tit" x="{W / 2}" y="78" text-anchor="middle">{t1}</text>'
    if t2:
        s += f'<text class="tit" x="{W / 2}" y="96" text-anchor="middle">{t2}</text>'
    if sub:
        s += f'<text class="sub" x="{W / 2}" y="{114 if t2 else 98}" text-anchor="middle">{sub}</text>'
    if it.get('uso'):
        etq = it['uso'] if isinstance(it['uso'], str) else '1 uso'
        ancho = max(70, 9 * len(etq) + 16)
        s += (f'<rect class="uso-r" x="{W - ancho + 8}" y="-10" width="{ancho}" height="20" rx="10"/>'
              f'<text class="uso-t" x="{W - ancho / 2 + 8}" y="4" text-anchor="middle">{etq}</text>')
    return s + '</g>'


def _rombo(x, y, it):
    r = 54
    return (f'<polygon class="rombo" points="{x},{y - r} {x + r + 16},{y} {x},{y + r} {x - r - 16},{y}"/>'
            f'<text class="rombo-t" x="{x}" y="{y - 3}" text-anchor="middle">{it["l1"]}</text>'
            f'<text class="rombo-t" x="{x}" y="{y + 13}" text-anchor="middle">{it["l2"]}</text>')


def _flecha(d, clase, punta, ang, px, py):
    return (f'<path class="{clase}" d="{d}"/>'
            f'<path class="{punta}" d="M0,-6 L10,0 L0,6 z" transform="translate({px},{py}) rotate({ang})"/>')


def _medio(it):
    return 70 if it['tipo'] == 'rombo' else 88   # media anchura del elemento


def svg(items, etiqueta):
    """items: [{'tipo':'nodo', icono,t1,t2,sub,uso} | {'tipo':'rombo', l1,l2, no:'texto nota' | ciclo:indice, si:'texto'}]"""
    pos = []
    for i in range(len(items)):
        fila, col = divmod(i, 5)
        x = XS[col] if fila % 2 == 0 else XS[4 - col]
        pos.append((x, Y0 + fila * DY, fila))
    filas = pos[-1][2] + 1
    partes, n = [], 0
    numeros = {}
    for i, it in enumerate(items):
        x, y, fila = pos[i]
        if it['tipo'] == 'nodo':
            n += 1
            numeros[i] = n
            partes.append(_nodo(x, y, n, it))
        else:
            partes.append(_rombo(x, y, it))
        # rama «No» de una decisión
        if it['tipo'] == 'rombo' and it.get('no'):
            arriba = fila == 0
            yb = y - 54 if arriba else y + 54
            yn = y - 74 if arriba else y + 74
            partes.append(_flecha(f'M{x},{yb} V{yn}', 'linea-no', 'punta-no', -90 if arriba else 90, x, yn))
            partes.append(f'<text class="etq no" x="{x + 8}" y="{y - 60 if arriba else y + 70}">No</text>')
            ry = y - 110 if arriba else y + 76
            partes.append(f'<g class="nota"><rect x="{x - 105}" y="{ry}" width="210" height="34" rx="8"/>'
                          f'<text x="{x}" y="{ry + 21}" text-anchor="middle">{it["no"]}</text></g>')
        # ciclo: vuelve a un paso anterior de la misma fila, por debajo
        if it['tipo'] == 'rombo' and it.get('ciclo') is not None:
            xd, yd, _ = pos[it['ciclo']]
            partes.append(_flecha(f'M{x},{y + 54} V{y + 92} H{xd} V{y + 74}', 'linea-si', 'punta-si', -90, xd, y + 74))
            partes.append(f'<text class="etq si" x="{min(x, xd) + 10}" y="{y + 86}">{it.get("textoCiclo", "Sí")}</text>')
        # flecha al siguiente
        if i + 1 < len(items):
            x2, y2, fila2 = pos[i + 1]
            sig = items[i + 1]
            es_ciclo = it['tipo'] == 'rombo' and it.get('ciclo') is not None
            clase, punta = ('linea-si', 'punta-si') if it['tipo'] == 'rombo' and not es_ciclo else ('linea-f', 'punta')
            if fila2 == fila:
                dirx = 1 if x2 > x else -1
                a, b = x + dirx * _medio(it), x2 - dirx * (_medio(sig) + 10)
                partes.append(_flecha(f'M{a},{y} H{b}', clase, punta, 0 if dirx > 0 else 180, b, y))
                if it['tipo'] == 'rombo':
                    partes.append(f'<text class="etq {"no" if es_ciclo else "si"}" x="{a + dirx * 10 - (0 if dirx > 0 else 24)}" y="{y - 8}">'
                                  f'{"No" if es_ciclo else "Sí"}</text>')
            else:
                # giro al final de la fila
                gx = XG if fila % 2 == 0 else 0
                dirx = 1 if fila % 2 == 0 else -1
                a = x + dirx * _medio(it)
                b = x2 + dirx * (_medio(sig) + 10)
                partes.append(_flecha(f'M{a},{y} H{gx} V{y2} H{b}', clase, punta, 180 if dirx > 0 else 0, b, y2))
    alto = filas * DY + 20
    return (f'<svg viewBox="-20 -30 1240 {alto}" role="img" aria-label="{etiqueta}">' + ''.join(partes) + '</svg>'), numeros
