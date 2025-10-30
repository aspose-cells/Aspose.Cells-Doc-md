---
title: Bloqueo de marca de agua de WordArt con Golang vía C++
linktitle: Bloqueo de marca de agua de WordArt
type: docs
weight: 170
url: /es/go-cpp/locking-wordart-watermark/
description: Aprenda cómo bloquear marcas de agua WordArt en hojas de cálculo de Excel usando Aspose.Cells for C++. Evite la edición, movimiento y selección de las marcas de agua programáticamente.
---

{{% alert color="primary" %}}

Las API de Aspose.Cells permiten agregar marcas de agua WordArt en la hoja de cálculo de tal manera que el WordArt se convierta en un objeto que puede mover y posicionar en la hoja de cálculo. También es posible bloquear el objeto WordArt para cualquier interacción como edición, movimiento y selección. Este artículo explica el uso del método [**Shape.SetLockedProperty**](https://reference.aspose.com/cells/go-cpp/shape/setlockedproperty/) para bloquear algunos aspectos de la marca de agua.

{{% /alert %}}

Las API de Aspose.Cells permiten bloquear ciertos aspectos de la marca de agua para que la interacción del usuario pueda ser limitada o completamente bloqueada. El siguiente fragmento de código demuestra el uso de la API Aspose.Cells for C++ para bloquear la selección, movimiento, edición y cambio de tamaño de la marca de agua creando una hoja de cálculo desde cero.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LockingWordartWatermark.go" >}}
