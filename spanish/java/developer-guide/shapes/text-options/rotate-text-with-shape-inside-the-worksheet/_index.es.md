---
title: Rotar Texto con Forma dentro de la Hoja de Cálculo
type: docs
weight: 110
url: /es/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Escenarios de uso posibles**

Puedes agregar texto dentro de cualquier forma utilizando Microsoft Excel. Si agregas una forma utilizando el antiguo Microsoft Excel 2003, entonces el texto no se rotará con la forma. Pero si agregas una forma utilizando versiones más recientes de Microsoft Excel como 2007, 2010, 2013 o 2016, etc., entonces el texto se rotará con la forma. Puedes controlar si el texto debe rotar con la forma o no utilizando la propiedad [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). El valor por defecto es **true** lo que significa que el texto se rotará con la forma, pero si lo configuras como **false**, entonces el texto no se rotará con la forma.

## **Rotar texto con forma dentro de la hoja de cálculo**

El siguiente código de muestra carga el [archivo Excel de muestra](64716919.xlsx) que tiene una forma de triángulo y su texto rota con la forma. Si abres el archivo Excel de muestra en Microsoft Excel y rotas la forma de triángulo, el texto también se rotará con ella. Luego, el código establece la propiedad [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) como **false** y lo guarda como [archivo Excel de salida](64716917.xlsx). Si abres ahora el archivo Excel de salida en Microsoft Excel y rotas la forma de triángulo, el texto no se rotará con ella. Por favor, consulta la siguiente captura de pantalla que muestra el efecto del código en el archivo Excel de muestra como referencia.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
