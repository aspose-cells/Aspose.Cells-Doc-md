---
title: Rotar Texto con Forma dentro de la Hoja de Cálculo
type: docs
weight: 1300
url: /es/python-net/rotate-text-with-shape-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Puedes agregar texto dentro de cualquier forma usando Microsoft Excel. Si agregas una forma en Microsoft Excel 2003, el texto no se rotará con la forma. Pero si agregas una forma en versiones más nuevas de Microsoft Excel como 2007, 2010, 2013 o 2016, etc., entonces el texto se rotará con la forma. Puedes controlar si el texto debe rotar con la forma o no usando la propiedad [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape). El valor predeterminado es verdadero, lo que significa que el texto se rotará con la forma, pero si lo estableces como falso, el texto no se rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716896.xlsx) que tiene una forma de triángulo y su texto se rota con la forma. Si abres el archivo de Excel de muestra en Microsoft Excel y giras la forma de triángulo, el texto también se rotará con él. Luego, el código establece la propiedad [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) como falso y lo guarda como [archivo de Excel de salida](64716897.xlsx). Si abres el archivo de Excel de salida en Microsoft Excel y giras la forma de triángulo, el texto no se rotará con él. Consulta la siguiente captura de pantalla que muestra el efecto del código en el archivo de Excel de muestra para referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
