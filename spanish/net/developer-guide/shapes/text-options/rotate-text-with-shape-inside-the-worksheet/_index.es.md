---
title: Rotar texto con forma dentro de la hoja de trabajo
type: docs
weight: 1300
url: /es/net/rotate-text-with-shape-inside-the-worksheet/
---
## **Posibles escenarios de uso**

Puede agregar texto dentro de cualquier forma usando Microsoft Excel. Si agrega forma usando el muy antiguo Microsoft Excel 2003, entonces el texto no rotará con la forma. Pero si agrega forma usando versiones más nuevas de Microsoft Excel, por ejemplo, 2007, 2010, 2013 o 2016, etc., entonces el texto rotará con forma. Puede controlar si el texto debe rotar con la forma o no usando el[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) propiedad. El valor por defecto es**verdadero**lo que significa que el texto rotará con la forma, pero si lo configura como**falso**, entonces el texto no rotará con la forma.

## **Rotar texto con forma dentro de la hoja de trabajo**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716896.xlsx) que tiene forma de triángulo y su texto gira con la forma. Si abre el archivo de muestra de Excel en Microsoft Excel y gira la forma del triángulo, el texto también girará con él. A continuación, el código establece el[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) propiedad como**falso** y lo guarda como[archivo de salida de Excel](64716897.xlsx). Si ahora abre el archivo de salida de Excel en Microsoft Excel y gira la forma del triángulo, el texto no girará con él. Consulte la siguiente captura de pantalla que muestra el efecto del código en un archivo de muestra de Excel como referencia.

![todo:imagen_alternativa_texto](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
