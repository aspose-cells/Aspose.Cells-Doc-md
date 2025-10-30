---
title: Cómo Usar el Parámetro de Rango en SmartMarkers
type: docs
weight: 10
url: /es/net/how-to-use-range-parameter-in-smart-markers/
---

## **Por qué Usar el Parámetro de Rango en Smart Markers**
El parámetro de rango en SmartMarkers se usa para controlar con precisión dónde y cómo se colocan los datos en una plantilla de Excel al llenarla con datos de una fuente (por ejemplo, JSON, bases de datos). Ayuda a gestionar la salida de datos dinámica, especialmente cuando se trata de arreglos de longitud variable o agrupamientos complejos.

1. Controlar la Colocación de Datos y Evitar Solapamientos: Cuando las fuentes de datos contienen arreglos dinámicos (por ejemplo, número variable de elementos por registro), el parámetro de rango asegura que los datos se llenen dentro de un rango de Excel definido, evitando desbordamientos en celdas o secciones adyacentes.

2. Manejar Fórmulas de Arreglos Dinámicos: Para operaciones como la transposición de arreglos dinámicos (por ejemplo, &=TRANSPOSE(DataArray)), el parámetro de rango garantiza que la salida se adapte al tamaño real de los datos sin dejar valores residuales (como ceros en campos vacíos) de operaciones anteriores.

3. Soportar Agrupamientos y Datos Jerárquicos: Cuando los datos requieren agrupamiento (por ejemplo, estructuras JSON anidadas), el parámetro de rango ayuda a definir áreas de salida jerárquicas. Por ejemplo, agrupar registros bajo una categoría principal sin ajustes manuales de filas. Sin un rango definido, SmartMarkers podría no representar con exactitud relaciones anidadas, especialmente si las fuentes de datos carecen de jerarquías explícitas.

4. Mejorar el Diseño y la Consistencia de la Plantilla: Especificando rangos, los usuarios aseguran que el formateo, las fórmulas y los bordes se apliquen de manera coherente al área de salida. Esto evita problemas como estilos inconsistentes o fórmulas rotas en los informes generados.

5. Optimizar el Rendimiento y Ordenamiento de Datos: El parámetro de rango permite a las herramientas ordenarlos previamente antes de llenar las plantillas, asegurando que los datos agrupados aparezcan en el orden correcto.

## **Cómo Usar el Parámetro de Rango en SmartMarkers**
A veces, necesitas ordenar y realizar otras operaciones en un rango en SmartMarkers. Aspose.Cells hace posible usar el parámetro de rango en SmartMarkers. Por favor, revisa [archivo de plantilla](range.xlsx), [archivo JSON](range.json) y la captura de pantalla del archivo Excel generado con el siguiente código.

|**La primera hoja del archivo range.xlsx mostrando smart markers.**|
| :- |
|![todo:image_alt_text](range_template.png)|

|**La captura de pantalla del archivo excel de salida.**|
| :- |
|![todo:image_alt_text](range_result.png)|

Datos json de la siguiente manera:
```json data
{
  "Groups": [
    {
      "Materials": [
        { 
	        "Name": "BBB", 
	        "DSSection": { "Name": "Item B" } 
	      },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item C" }
        },
        {
          "Name": "AAA",
          "DSSection": { "Name": "Item A" }
        },        
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "CCC",
          "DSSection": { "Name": "Item A" }
        },
        {
          "Name": "BBB",
          "DSSection": { "Name": "Item A" }
        },
        { 
	        "Name": "AAA", 
	        "DSSection": { "Name": "Item C" } 
        }
      ]
    }
  ]
}
```
El ejemplo que sigue muestra cómo funciona esto.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-Using-Range-Parameter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
