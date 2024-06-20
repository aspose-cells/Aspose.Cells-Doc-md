---
title: Configuración de página
type: docs
weight: 80
url: /es/reportingservices/page-setup/
---

La configuración incluye dos secciones y 8 tipos de propiedades de configuración de página. Estas propiedades incluyen nombre, índice, AjustarAltoPáginas, AjustarAnchoPáginas, MargenSuperior, MargenPie, MargenEncabezado, MargenInferior, MargenIzquierdo y MargenDerecho.

- **nombre** representa el nombre del informe, representa el informe completo cuando el nombre está en blanco.
- **índice** representa el índice de la hoja de trabajo del archivo de Excel exportado.
- **FitToPagesTall** representa la cantidad de páginas en altura a la que se escalará la hoja de trabajo al imprimirse.
- **FitToPagesWide** representa la cantidad de páginas en anchura a la que se escalará la hoja de trabajo al imprimirse.
- **FooterMargin** representa la distancia desde la parte inferior de la página hasta el pie de página, en unidades de centímetros.
- **HeaderMargin** representa la distancia desde la parte superior de la página hasta el encabezado, en unidades de centímetros.
- **LeftMargin** representa el tamaño del margen izquierdo, en unidades de centímetros.
- **RightMargin** representa el tamaño del margen derecho, en unidades de centímetros.
- **TopMargin** representa el tamaño del margen superior, en unidades de centímetros.
- **BottomMargin** representa el tamaño del margen inferior, en unidades de centímetros.

Ejemplo de configuración de página:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
