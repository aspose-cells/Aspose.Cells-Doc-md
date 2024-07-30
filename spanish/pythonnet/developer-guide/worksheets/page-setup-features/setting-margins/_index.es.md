---
title: Configurando Márgenes
type: docs
weight: 20
url: /es/python-net/setting-margins/
description: En este artículo aprenderás cómo establecer los márgenes de una hoja de cálculo de Excel utilizando un código de ejemplo. También aprenderás cómo establecer programáticamente los márgenes para el centro de la página, los márgenes de encabezado y pie de página de la configuración de página usando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, establecer margen de hoja de cálculo de Excel en centro, establecer margen de encabezado y pie de página de la hoja de cálculo usando Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET soporta completamente las opciones de configuración de página de Microsoft Excel. Los desarrolladores pueden necesitar configurar los ajustes de configuración de página para las hojas de cálculo para controlar el proceso de impresión. Este tema trata sobre cómo utilizar Aspose.Cells para Python via .NET para configurar los márgenes de página.

{{% /alert %}}

## **Cómo establecer márgenes**

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene la colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona la propiedad [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) utilizada para establecer las opciones de configuración de página de una hoja de cálculo. El atributo [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) es un objeto de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) que permite a los desarrolladores establecer diferentes opciones de diseño de página para una hoja de cálculo impresa. La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) proporciona varias propiedades y métodos utilizados para establecer opciones de configuración de página.

## **Cómo establecer márgenes de página**

Establezca los márgenes de página (izquierdo, derecho, arriba, abajo) utilizando los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup). A continuación se enumeran algunos de los métodos que se utilizan para especificar los márgenes de página:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **Cómo centrar en la página**

Es posible centrar algo en una página horizontal y verticalmente. Para ello, hay algunos miembros útiles de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup), [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) y [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **Cómo establecer márgenes de encabezado y pie de página**

Establezca los márgenes de encabezado y pie de página con los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) como [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) y [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
