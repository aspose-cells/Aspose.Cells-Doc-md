---
title: Configuración de página
type: docs
weight: 80
url: /es/reportingservices/page-setup/
---
La configuración incluye dos secciones y 8 tipos de propiedades de configuración de página. Estas propiedades incluyen nombre, índice, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin y RightMargin.

- **nombre** representa el nombre del informe, representa el informe completo cuando el nombre está en blanco.
- **índice** representa el índice de la hoja de trabajo del archivo de Excel exportado.
- **FitToPagesTall** representa el número de páginas de altura a las que se escalará la hoja de cálculo cuando se imprima.
- **FitToPagesWide** representa el número de páginas de ancho a las que se escalará la hoja de trabajo cuando se imprima.
- **Margen de pie de página**representa la distancia desde la parte inferior de la página hasta el pie de página, en la unidad de centímetros.
- **Margen de encabezado** representa la distancia desde la parte superior de la página hasta el encabezado, en la unidad de centímetros.
- **Margen izquierdo** representa el tamaño del margen izquierdo, en la unidad de centímetros.
- **Margen derecho** representa el tamaño del margen derecho, en la unidad de centímetros.
- **Margen superior** representa el tamaño del margen superior, en la unidad de centímetros.
- **Margen inferior** representa el tamaño del margen inferior, en la unidad de centímetros.

Ejemplo de configuración de PageSetup:

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
