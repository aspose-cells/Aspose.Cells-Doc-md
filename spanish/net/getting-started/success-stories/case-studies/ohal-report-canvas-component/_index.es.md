---
title: Componente de Informe Canvas Ohal
type: docs
weight: 30
url: /es/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[Informe en PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Uso de Aspose.Cells en el Componente de Informe Canvas**

Robert Chilvers, 17 de marzo de 2008

{{% /alert %}}

## **Antecedentes del producto**

El Componente de Informe Canvas permite al usuario crear informes visuales basados en un conjunto de datos pre-cargado. El usuario puede agregar diferentes componentes a su lienzo, incluyendo imágenes, cuadros de texto, gráficos y tablas, luego especifica los datos y cómo se deben agregar. El usuario luego puede reorganizar y redimensionar los objetos para que encajen en su página. El usuario puede especificar paletas de colores y guardar plantillas para uso futuro. Aspose.Cells se utiliza para exportar todos los objetos en el lienzo a Excel con los datos correctos. El componente está escrito en VB.Net en Visual Studio 2008.

## **Escenario de requisitos**

Seleccionamos Aspose.Cells debido a sus capacidades casi completas de exportación de Microsoft Excel. Lo más importante para nosotros es la capacidad de exportar gráficos y tablas, especialmente en Microsoft Excel 2007; estas características estaban ausentes en otros componentes de terceros.

## **Implementación de la solución**

Cada objeto en el lienzo del informe tiene una función a la que se le pasa una instancia de la hoja de cálculo de Aspose.Cells y se agrega a sí misma a la hoja de cálculo. Cuando el usuario solicita una exportación, se inicializan el libro de trabajo y las hojas de cálculo, y se llama a esta función para cada objeto en el lienzo del informe.

## **Beneficios**

Aspose.Cells nos permitió construir todo el libro de trabajo de Excel de forma totalmente independiente de Excel, y luego guardar el libro de trabajo en el formato seleccionado por el usuario. Esto nos ahorró horas de depuración de la interacción al usar el Excel interop e implementar diferentes rutinas para guardar en distintas versiones de Excel.

## **Implementación Futura**

Es probable que utilicemos Aspose.Cells para cargar y guardar todos los archivos de Excel. Esto incluirá la carga de plantillas de datos y la exportación de resultados.

## **Conclusión**

{{% alert color="primary" %}}

Hasta ahora, no hemos tenido problemas utilizando los componentes Aspose.Cells y el componente debería ahorrarnos tiempo de desarrollo a corto y largo plazo. Las consultas de soporte y ventas han sido respondidas rápidamente y de manera útil.

{{% /alert %}}
