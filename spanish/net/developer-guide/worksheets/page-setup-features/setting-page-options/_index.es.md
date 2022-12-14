---
title: Configuración de opciones de página
type: docs
weight: 10
url: /es/net/setting-page-options/
---
{{% alert color="primary" %}}

A veces, es necesario configurar los ajustes de configuración de la página para que las hojas de trabajo controlen la impresión. Estos ajustes de configuración de página ofrecen varias opciones.

{{% /alert %}}

## **Configuración de opciones de página**

Las opciones de configuración de página son totalmente compatibles con Aspose.Cells. Este artículo explica cómo configurar las opciones de página con Aspose.Cells y muestra ejemplos de código para configurar:

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

 los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la clase proporciona la[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) propiedad que se utiliza para establecer las opciones de configuración de página de la hoja de cálculo. De hecho, esto[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) La propiedad es un objeto de la[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase utilizada para establecer diferentes opciones de diseño de página para una hoja de trabajo impresa. los[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)class proporciona varias propiedades que se utilizan para establecer las opciones de configuración de la página. Algunas de estas propiedades se analizan a continuación.

### **Orientación de la página**

 La orientación de la página se puede establecer en vertical u horizontal mediante el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**Orientación**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) propiedad. los[**Orientación**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/orientation) propiedad acepta uno de los valores predefinidos en el[**Tipo de orientación de página**](https://reference.aspose.com/cells/net/aspose.cells/pageorientationtype)enumeración, que se enumeran a continuación.

|**Tipos de orientación de página**|**Descripción**|
|:- |:- |
|Paisaje|Orientación horizontal|
|Retrato|Orientación Vertical|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-PageOrientation-1.cs" >}}

### **Factor de escala**

 Es posible reducir o aumentar el tamaño de una hoja de trabajo ajustando el factor de escala con el[**PageSetup.Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom)propiedad.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ScalingFactor-1.cs" >}}

### **Opciones de FitToPages**

 Para ajustar el contenido de la hoja de trabajo a un número específico de páginas, use el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall) y[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide)propiedades. Estas propiedades también se utilizan para escalar hojas de cálculo.

{{% alert color="primary" %}}

 Puede elegir el[**FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopagestall)/[**FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/fittopageswide) o el[**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/zoom) propiedad, pero no ambas al mismo tiempo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-FitToPagesOptions-1.cs" >}}

### **Tamaño de papel**

 Establezca el tamaño de papel en el que se imprimirán las hojas de trabajo utilizando el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**Tamaño de papel**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) propiedad. los[**Tamaño de papel**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/papersize) propiedad acepta uno de los valores predefinidos en el[**Tipo de tamaño de papel**](https://reference.aspose.com/cells/net/aspose.cells/papersizetype)enumeración, que se enumeran a continuación.

|**Tipos de tamaño de papel**|**Descripción**|
|:- |:- |
|PapelCarta|Carta (8-1/2 pulg. x 11 pulg.)|
|De PapelCartaPequeños|Carta pequeña (8-1/2 pulg. x 11 pulg.)|
|Tabloide de papel|Tabloide (11 pulg. x 17 pulg.)|
|libro mayor|Libro mayor (17 pulg. x 11 pulg.)|
|PapelLegal|Legal (8-1/2 pulg. x 14 pulg.)|
|PaperStatement|Declaración (5-1/2 pulg. x 8-1/2 pulg.)|
|PapelEjecutivo|Ejecutivo (7-1/4 pulg. x 10-1/2 pulg.)|
|PapelA3|A3 (297 mm x 420 mm)|
|PapelA4|A4 (210 mm x 297 mm)|
|PapelA4Pequeño|A4 pequeño (210 mm x 297 mm)|
|PapelA5|A5 (148 mm x 210 mm)|
|PapelB4|JIS B4 (257 mm x 364 mm)|
|PapelB5|JIS B5 (182 mm x 257 mm)|
|PapelFolio|Folio (8-1/2 pulg. x 13 pulg.)|
|PaperQuarto|Cuarto (215 mm x 275 mm)|
|Papel10x14|10 pulgadas x 14 pulgadas|
|Papel11x17|11 pulgadas x 17 pulgadas|
|Nota de papel|Nota (8-1/2 pulg. x 11 pulg.)|
|PapelSobre9|Sobre #9 (3-7/8 pulg. x 8-7/8 pulg.)|
|PapelSobre10|Sobre #10 (4-1/8 pulg. x 9-1/2 pulg.)|
|PapelSobre11|Sobre #11 (4-1/2 pulg. x 10-3/8 pulg.)|
|PapelSobre12|Sobre #12 (4-1/2 pulg. x 11 pulg.)|
|PapelSobre14|Sobre #14 (5 pulg. x 11-1/2 pulg.)|
|PapelCHoja|Hoja de tamaño C|
|PapelDHoja|Hoja de tamaño D|
|PapelEHoja|Hoja de tamaño E|
|PapelSobreDL|Sobre DL (110 mm x 220 mm)|
|PapelSobreC5|Sobre C5 (162 mm x 229 mm)|
|PapelSobreC3|Sobre C3 (324 mm x 458 mm)|
|PapelSobreC4|Sobre C4 (229 mm x 324 mm)|
|PapelSobreC6|Sobre C6 (114 mm x 162 mm)|
|PapelSobreC65|Sobre C65 (114 mm x 229 mm)|
|PapelSobreB4|Sobre B4 (250 mm x 353 mm|
|PapelSobreB5|Sobre B5 (176 mm x 250 mm)|
|PapelSobreB6|Sobre B6 (176 mm x 125 mm)|
|De PapelSobreItalia|Sobre Italia (110 mm x 230 mm)|
|De PapelSobreMonarca|Sobre monarca (3-7/8 pulg. x 7-1/2 pulg.)|
|De PapelSobrePersonal|Sobre (3-5/8 pulg. x 6-1/2 pulg.)|
|PaperFanfoldUS|Plegado estándar de EE. UU. (14-7/8 pulg. x 11 pulg.)|
|PaperFanfoldStdAlemán|Plegado estándar alemán (8-1/2 pulg. x 12 pulg.)|
|PapelFanfoldLegalAlemán|Folleto en acordeón alemán legal (8-1/2 pulg. x 13 pulg.)|
|PapelISOB4|B4 (ISO) 250 x 353 mm|
|De PapelJaponésPostal|Postal japonesa (100 mm x 148 mm)|
|Papel9x11|9 pulgadas x 11 pulgadas|
|Papel10x11|10 pulgadas x 11 pulgadas|
|Papel15x11|15 pulgadas x 11 pulgadas|
|PapelSobreInvitar|Invitación de sobre (220 mm x 220 mm)|
|PapelCartaExtra|Carta EE. UU. Extra 9 \275 x 12 pulgadas|
|PapelLegalExtra|Extra legal de EE. UU. 9 \275 x 15 pulgadas|
|PapelTabloideExtra|Tabloide de EE. UU. Extra 11,69 x 18 pulgadas|
|PapelA4Extra|A4 Extra 9,27 x 12,69 pulgadas|
|De PapelCartaTransversal|Carta Transversal 8 \275 x 11 in|
|PapelA4Transversal|A4 Transversal 210 x 297 mm|
|PapelCartaExtraTransversal|Carta Extra Transversal 9\275 x 12 in|
|PapelSuperA|Súper A/Súper A/A4 227 x 356 mm|
|PaperSuperB|SuperB/SuperB/A3 305 x 487 mm|
|PaperLetterPlus|Carta de EE. UU. Plus 8,5 x 12,69 pulgadas|
|PapelA4Plus|A4 Plus 210 x 330 mm|
|PapelA5Transversal|A5 Transversal 148 x 210 mm|
|PapelJISB5Transversal|B5 (JIS) Transversal 182 x 257 mm|
|PapelA3Extra|A3 Extra 322 x 445 mm|
|PapelA5Extra|A5 Extra 174 x 235 mm|
|PapelISOB5Extra|B5 (ISO) Extra 201 x 276 mm|
|PapelA2|A2 420 x 594 mm|
|PapelA3Transversal|A3 Transversal 297 x 420 mm|
|PapelA3ExtraTransversal|A3 Extra Transversal 322 x 445 mm|
|PapelJaponésDoblePostal|Postal doble japonesa 200 x 148 mm|
|PapelA6|A6 105 x 148 mm|
|PapelJaponésSobreKaku2|Sobre Japonés Kaku #2|
|PapelJaponésSobreKaku3|Sobre Japonés Kaku #3|
|PapelJaponésSobreChou3|Sobre Japonés Chou #3|
|PapelJaponésSobreChou4|Sobre Japonés Chou #4|
|PapelCartaRotado|11in x 8.5in|
|PapelA3Rotado|420 mm x 297 mm|
|PapelA4Rotado|297 mm x 210 mm|
|PapelA5Rotado|210 mm x 148 mm|
|PapelJISB4Rotado|B4 (JIS) Rotado 364 x 257 mm|
|PapelJISB5Rotado|B5 (JIS) Girado 257 x 182 mm|
|papeljaponéspostalgirado|Postal japonesa girada 148 x 100 mm|
|papeljaponésdoblepostalgirado|Postal japonesa doble girada 148 x 200 mm|
|PapelA6Rotado|A6 Girado 148 x 105 mm|
|PapelJaponésSobreKaku2Rotado|Sobre Japonés Kaku #2 Girado|
|papeljaponéssobrekaku3girado|Sobre Japonés Kaku #3 Girado|
|PapelJaponésSobreChou3Rotado|Sobre Japonés Chou #3 Girado|
|PapelJaponésSobreChou4Rotado|Sobre Japonés Chou #4 Girado|
|PapelJISB6|B6 (JIS) 128 x 182 mm|
|PapelJISB6Rotado|B6 (JIS) Girado 182 x 128 mm|
|Papel12x11|12 x 11 pulgadas|
|PapelJaponésSobreUsted4|Sobre Japonés Tú #4|
|PapelJaponésSobreUsted4Rotado|Sobre japonés que giraste #4|
|PapelPRC16K|China 16K 146 x 215 mm|
|PapelPRC32K|China 32K 97 x 151 mm|
|PapelPRCBig32K|PRC 32K (Grande) 97 x 151 mm|
|PaperPRCEvelope1|PRC Sobre #1 102 x 165 mm|
|PaperPRCEvelope2|Sobre PRC #2 102 x 176 mm|
|PaperPRCEvelope3|Sobre PRC #3 125 x 176 mm|
|PaperPRCEvelope4|PRC Sobre #4 110 x 208 mm|
|PaperPRCEvelope5|PRC Sobre #5 110 x 220 mm|
|PaperPRCEvelope6|Sobre PRC #6 120 x 230 mm|
|PaperPRCEvelope7|Sobre PRC #7 160 x 230 mm|
|PapelPRCEnvelope8|Sobre PRC #8 120 x 309 mm|
|PapelPRCEnvelope9|Sobre PRC #9 229 x 324 mm|
|PaperPRCEvelope10|Sobre PRC #10 324 x 458 mm|
|PapelPRC16KRotado|PRC 16K girado|
|PapelPRC32KRotado|PRC 32K girado|
|PaperPRCBig32KRotated|PRC 32K (grande) girado|
|PaperPRCEnvelope1Rotated|Sobre PRC #1 Girado 165 x 102 mm|
|PaperPRCEvelope2Rotated|Sobre PRC #2 Girado 176 x 102 mm|
|PaperPRCEnvelope3Rotated|Sobre PRC #3 Girado 176 x 125 mm|
|PaperPRCEnvelope4Rotated|Sobre PRC #4 Girado 208 x 110 mm|
|PaperPRCEnvelope5Rotated|PRC Sobre #5 Girado 220 x 110 mm|
|PaperPRCEnvelope6Rotated|PRC Sobre #6 Girado 230 x 120 mm|
|PaperPRCEnvelope7Rotated|PRC Sobre #7 Girado 230 x 160 mm|
|PaperPRCEnvelope8Rotated|PRC Sobre #8 Girado 309 x 120 mm|
|PaperPRCEnvelope9Rotated|Sobre PRC #9 Girado 324 x 229 mm|
|PaperPRCEnvelope10Rotated|Sobre PRC #10 girado 458 x 324 mm|
|PapelB3|habitual B3 (13,9 x 19,7 pulgadas)|
|PapelNegocioTarjeta|Tarjeta de visita (90 mm x 55 mm)|
|Papel Térmico|Térmica (3 x 11 pulgadas)|
|Disfraz|Representa el tamaño de papel personalizado.|

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ManagePaperSize-1.cs" >}}

### **Calidad de impresión**

 Establezca la calidad de impresión de las hojas de trabajo que se imprimirán con el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**Calidad de impresión**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/printquality)propiedad. La unidad de medida de la calidad de impresión es Puntos por pulgada (DPI).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetPrintQuality-1.cs" >}}

### **Número de la primera página**

 Inicie la numeración de las páginas de la hoja de trabajo usando el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) clase'[**NúmeroPrimeraPágina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber) propiedad. los[**NúmeroPrimeraPágina**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/firstpagenumber)Esta propiedad establece el número de página de la primera página de la hoja de trabajo y las páginas siguientes se numeran en orden ascendente.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetFirstPageNumber-1.cs" >}}
