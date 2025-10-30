---
title: Copiar solo estilo de rango con Golang vía C++
linktitle: Copiar solo estilo de rango
type: docs
weight: 620
url: /es/go-cpp/copy-range-style-only/
description: Aprende cómo copiar solo el estilo de un rango en Excel usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

[Copiar solo datos del rango](/cells/es/cpp/copy-range-data-only/) y [Copiar datos del rango con estilo](/cells/es/cpp/copy-range-data-with-style/) explican cómo copiar datos de un rango a otro por sí solo o completo con formato. También es posible copiar solo el formato. Este artículo muestra cómo.

{{% /alert %}} 

Este ejemplo crea un libro de trabajo, lo llena con datos y copia solo el estilo de un rango.

1. Crear un rango.
1. Crea un objeto [**Style**](https://reference.aspose.com/cells/go-cpp/style/) con atributos de formato especificados.
1. Aplica el formato de estilo al rango.
1. Crear un segundo rango de celdas.
1. Copiar el formato del primer rango al segundo rango.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRangeStyleOnly.go" >}}
