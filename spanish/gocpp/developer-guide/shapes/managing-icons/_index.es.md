---
title: Añadir iconos a la hoja de cálculo con Golang mediante C++
linktitle: Gestionar iconos
type: docs
weight: 100
url: /es/go-cpp/insert-svg-to-excel/
description: Aprende cómo agregar iconos a hojas de cálculo de Excel usando Aspose.Cells con Golang vía C++
---

## Agregar iconos a la hoja de cálculo en Aspose.Cells

Si necesita usar [Aspose.Cells](https://products.aspose.com/cells/) para agregar 'iconos' en un archivo de Excel, este documento puede ofrecerle ayuda.

La interfaz de Excel correspondiente a la operación de insertar icono es la siguiente:

![](1.png)

- Seleccione la posición del icono a insertar en la hoja de cálculo
- Haga clic izquierdo *Insertar*->*Iconos*
- En la ventana que se abre, seleccione el icono en el rectángulo rojo en la figura anterior
- Haz clic izquierdo en *Insertar*, se insertará en el archivo de Excel.

El efecto es el siguiente:

![](2.png)

Aquí, hemos preparado *código de ejemplo* para ayudarte a insertar íconos usando [Aspose.Cells](https://products.aspose.com/cells/). También hay un [archivo de ejemplo](sample.xlsx) y un [archivo de recursos](icon.zip). Usamos la interfaz de Excel para insertar un ícono con el mismo efecto visual que el [archivo de recursos](icon.zip) en el [archivo de ejemplo](sample.xlsx).

### C++

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingIcons.go" >}}
Cuando ejecute el código anterior en su proyecto, obtendrá los siguientes resultados:

![](3.png)
