---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/net/lock-or-unlock-shapes/
description: Este artículo te muestra el código que explica cómo bloquear o desbloquear formas para protegerlas utilizando la biblioteca Aspose.Cells.
keywords: C# Bloquear Formas para Protegerlas, Cómo bloquear o desbloquear formas usando C#, Bloquear o desbloquear formas para Protegerlas en C#.
---

## **Escenarios de uso posibles**

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada. 

Bloquear formas en una hoja de cálculo o documento puede ser beneficioso por varias razones:
1. Prevenir Cambios Accidentales: Bloquear formas asegura que no sean movidas, redimensionadas o eliminadas accidentalmente por los usuarios. Esto es especialmente importante en documentos complejos donde las formas pueden usarse para anotaciones, ilustraciones o como parte del diseño del documento.
1. Mantener el diseño y la distribución: Las formas suelen desempeñar un papel crucial en el diseño visual de un documento. Al bloquearlas se conserva la apariencia prevista, garantizando que el documento siga siendo profesional y atractivo visualmente.
1. Integridad de los datos: En las hojas de cálculo, las formas se pueden utilizar para resaltar puntos de datos importantes, agregar comentarios o proporcionar explicaciones visuales. Bloquear estas formas asegura que la información contextual que proporcionan siga siendo precisa e intacta.
1. Consistencia en documentos compartidos: Al colaborar en documentos, diferentes usuarios pueden tener diferentes niveles de experiencia. Bloquear formas ayuda a mantener la consistencia en todo el documento al evitar modificaciones no deseadas.
1. Seguridad: En documentos sensibles, bloquear formas puede formar parte de una estrategia más amplia para proteger la información. Por ejemplo, en informes financieros o documentos legales, las formas bloqueadas se pueden utilizar para proteger anotaciones o puntos destacados específicos que proporcionan un contexto crítico.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas. Este artículo presentará detalladamente cómo bloquear y desbloquear formas específicas.

## **Cómo bloquear formas para protegerlas en Excel**

Así es como puedes bloquear celdas en Microsoft Excel:

1. Abra su archivo de Excel: Abra el archivo de Excel que contiene las formas que desea bloquear.

1. Seleccione la forma: Haga clic en la forma que desea bloquear. También puede seleccionar varias formas manteniendo presionada la tecla Ctrl y haciendo clic en cada forma.

1. Abra el panel de formato de forma: Haga clic derecho en la forma seleccionada(s) y elija "Tamaño y propiedades". Alternativamente, puede ir a la pestaña "Formato" en la Cinta de opciones y, en el grupo "Tamaño", haga clic en el lanzador de cuadros de diálogo (una pequeña flecha) para abrir el panel "Formato de forma".
1. Bloquee la forma: En el panel "Formato de forma", vaya a la pestaña "Tamaño y Propiedades" (el icono parece un cuadrado con flechas). En la sección "Propiedades", marque la casilla de "Bloqueado".
<br>
<img src="1.png" width=60% />
1. Protege la hoja de cálculo: Ve a la pestaña "Revisar" en la Cinta de opciones. Haz clic en "Proteger hoja". Establece una contraseña (opcional) y elige los permisos que deseas permitir (por ejemplo, seleccionar celdas bloqueadas, formatear celdas, etc.). Haz clic en "Aceptar".
<br>
<img src="2.png" width=60% />

## **Cómo bloquear todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo específica, utilice el método [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Cómo desbloquear formas específicas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja de cálculo protegida, use [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), como se muestra en el siguiente código de ejemplo.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) solo tiene sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

