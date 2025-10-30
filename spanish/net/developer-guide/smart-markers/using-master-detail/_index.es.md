---
title: Importación inteligente de datos maestros y detalles en Excel con marcadores inteligentes
type: docs
weight: 30
url: /es/net/how-to-use-master-and-details-with-smart-markers/
---

## **Escenarios de uso posibles**
A veces, quieres generar informes dinámicos en Excel, que incluyen un panel principal completo y varias hojas detalladas de granularidad fina. Entre ellas, una sola tabla principal presenta una visión general, que puede mostrar varias variantes de productos, y cada hoja detallada correspondiente proporciona datos específicos y profundos para una sola variante. Aspose.Cells puede satisfacer perfectamente tus necesidades a través de maestros y detalles con marcadores inteligentes.


## **Parámetros de marcadores inteligentes para maestros y detalles**
Para importar datos maestros y detalles en Excel, debes usar los siguientes parámetros de marcadores inteligentes:

| Parámetro | Descripción | Valores aceptables (Sintaxis) | Restricciones | Opcionalidad | Comportamiento predeterminado | Restricciones de Excel |
| --- | --- | --- | --- | --- | --- | --- |
| `DetailSheet` | Especifica el nombre de la hoja de detalles almacenada en el archivo de plantilla. | Valor de cadena | El valor debe ser nulo o el nombre de la hoja. Si es nulo, esta es una hoja de detalles. Debe ser un valor de cadena simple. No se soporta variable. | Si se omite, no es hoja maestra ni de detalles. | Hoja de trabajo normal, no maestra ni de detalles. | |
| `DetailTable` | Especifica el nombre de la tabla de la hoja de detalles en el archivo de plantilla. | Valor de cadena | | Si se omite, el marcador inteligente en la hoja de detalles debe ser similar a la hoja maestra, de lo contrario, no podemos encontrar la fuente de datos. | Si se omite, el marcador inteligente en la hoja de detalles debe ser similar a la hoja maestra, de lo contrario, no podemos encontrar la fuente de datos. | |
| `DetailSheetNewName` | Especifica el nombre de la hoja de detalles recién creada. | Expresión similar a fórmula de Excel | Debe ser una fórmula válida para Excel si reemplazamos la variable ({a.bc}) por un valor simple. | Si se omite, las nuevas hojas serán Sheet1, Sheet2... | Si se omite, las nuevas hojas serán Sheet1, Sheet2... | El nombre debe ser un nombre válido para hoja de trabajo. |
| `DetailLink` | Indica si se deben agregar hipervínculos a la ubicación de los datos importados. | | | Si se omite, no agregar hipervínculos a la ubicación de los datos importados. | Si se omite, no agregar hipervínculos a la ubicación de los datos importados. | |

## **Cómo usar maestros y detalles cuando el maestro y los detalles están en una sola hoja de trabajo**
A veces, necesitas importar datos maestros y detalles a Excel en SmartMarkers. Aspose.Cells hace posible usar parámetros de maestros y detalles en SmartMarkers. Por favor, revisa [archivo de plantilla](MasterDetailInOneSheet.xlsx), [archivo JSON](MasterDetailData.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja de template.xlsx.**|
| :- |
|![todo:image_alt_text](1.png)|

|**La primera hoja del archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](2.png)|

|**La segunda hoja del archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](3.png)|

Datos json de la siguiente manera:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InOneSheet.cs" >}}

## **Cómo usar maestros y detalles cuando el maestro y los detalles están en hojas de trabajo diferentes**
A veces, necesitas importar datos maestros y detalles a Excel en SmartMarkers. Aspose.Cells hace posible usar parámetros de maestros y detalles en SmartMarkers. Por favor, revisa [archivo de plantilla](MasterDetailInTwoSheets.xlsx), [archivo JSON](MasterDetailData.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja maestra del archivo plantilla.xlsx.**|
| :- |
|![todo:image_alt_text](4.png)|

|**La segunda hoja maestra del archivo plantilla.xlsx.**|
| :- |
|![todo:image_alt_text](5.png)|

|**La hoja de detalles del archivo plantilla.xlsx.**|
| :- |
|![todo:image_alt_text](6.png)|

|**La primera hoja maestra del archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](7.png)|

|**La segunda hoja maestra del archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](8.png)|

|**La hoja de detalles de la primera hoja maestra en el archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](9.png)|

|**La primera hoja de detalles de la segunda hoja maestra en el archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](10.png)|

|**La segunda hoja de detalles de la segunda hoja maestra en el archivo Excel de salida.**|
| :- |
|![todo:image_alt_text](11.png)|

Datos json de la siguiente manera:
```json data
{
	"node": {
		"Styles1": [
			{
				"StyleID": "1style001",
				"StyleName": "StyleName1",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			}
		],
		"Styles2": [
			{
				"StyleID": "2style001",
				"StyleName": "Cotton StyleName2",
				"Quantity": 6,
				"UnitPrice": 18.45,
				"MaterialType":"Cotton"
			},
			{
				"StyleID": "2style002",
				"StyleName": "Denim StyleName2",
				"Quantity": 8,
				"UnitPrice": 58.8,
				"MaterialType":"Denim"
			}
		]
	}
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Master-Details-InDifferentSheets.cs" >}}
