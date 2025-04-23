---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/net/lock-or-unlock-shapes/
description: Este artículo te muestra código que explica cómo bloquear o desbloquear formas para protegerlas usando la biblioteca Aspose.Cells.
keywords: C# Bloquear formas para protegerlas, cómo bloquear o desbloquear formas usando C#, bloquear o desbloquear formas para protegerlas en C#.
---

## **Escenarios de uso posibles**

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada. 

Bloquear formas en una hoja de cálculo o documento puede ser beneficioso por varias razones:
1. Prevenir cambios accidentales: bloquear formas asegura que no sean movidas, redimensionadas o eliminadas accidentalmente por los usuarios. Esto es especialmente importante en documentos complejos donde las formas pueden usarse para anotaciones, ilustraciones o como parte del diseño del documento.
1. Mantener el diseño y la estética: las formas a menudo juegan un papel crucial en el diseño y la apariencia visual de un documento. Bloquearlas preserva la apariencia deseada, asegurando que el documento se vea profesional y atractivo.
1. Integridad de datos: en hojas de cálculo, las formas pueden usarse para resaltar puntos de datos importantes, agregar comentarios o proporcionar explicaciones visuales. Bloquear estas formas garantiza que la información contextual que proporcionan permanezca precisa e intacta.
1. Consistencia en documentos compartidos: al colaborar en documentos, diferentes usuarios pueden tener diferentes niveles de experiencia. Bloquear formas ayuda a mantener la coherencia en todo el documento evitando alteraciones no intencionadas.
1. Seguridad: en documentos sensibles, bloquear formas puede ser parte de una estrategia más amplia para proteger la información. Por ejemplo, en informes financieros o documentos legales, las formas bloqueadas pueden usarse para salvaguardar anotaciones o puntos destacados críticos.

A veces, necesitas poder modificar ciertas formas en ciertas hojas protegidas, en cuyo caso, necesitas desbloquear esas formas. Este artículo introducirá en detalle cómo bloquear y desbloquear formas específicas.

## **Cómo bloquear formas para protegerlas en Excel**

Así puedes bloquear celdas en Microsoft Excel:

1. Abre tu archivo de Excel: abre el archivo de Excel que contiene las formas que deseas bloquear.

1. Selecciona la forma: haz clic en la forma que deseas bloquear. También puedes seleccionar varias formas manteniendo presionada la tecla Ctrl y haciendo clic en cada forma.

1. Abre el panel de formato de formas: haz clic derecho en la(s) forma(s) seleccionadas y elige "Tamaño y propiedades." Alternativamente, puedes ir a la pestaña "Formato" en la cinta de opciones, y en el grupo "Tamaño", hacer clic en el lanzador de diálogo (una pequeña flecha) para abrir el panel "Formato de forma".
1. Bloquea la forma: en el panel "Formato de forma", ve a la pestaña "Tamaño y propiedades" (el ícono parece un cuadrado con flechas). En la sección "Propiedades", marca la casilla de "Bloqueado."
<br>
<img src="1.png" width=60% />
1. Protege la hoja de trabajo: Ve a la pestaña "Revisar" en la cinta de opciones. Haz clic en "Proteger hoja". Establece una contraseña (opcional) y elige los permisos que deseas permitir (por ejemplo, seleccionar celdas bloqueadas, formatear celdas, etc.). Haz clic en "Aceptar".
<br>
<img src="2.png" width=60% />

## **Cómo bloquear todas las formas en una hoja especificada**

Para proteger todas las formas en una hoja de cálculo específica, utilice el método [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Cómo desbloquear formas específicas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja de cálculo protegida, use [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), como se muestra en el siguiente código de ejemplo.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) solo tiene sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

{{< app/cells/assistant language="csharp" >}}
