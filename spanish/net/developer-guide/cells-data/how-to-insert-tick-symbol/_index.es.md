---
title: Cómo Insertar símbolo de marca de verificación
type: docs
weight: 10
url: /es/net/how-to-insert-tick-symbol-to-excel/
description: Este artículo introducirá cómo insertar el símbolo de marca de verificación con la API Aspose.Cells for .NET.
keywords: Copia y pega el símbolo de marca de verificación, usa el menú de símbolo o insertar, ingresa un código Alt, usa Autocorrección o atajos, utiliza el panel de emojis/símbolos, agrega una marca en una casilla / casilla de votación
---

## **Escenarios de uso posibles**
Insertar un símbolo de marca de verificación (✓) puede tener varios propósitos dependiendo del contexto. Aquí hay algunas razones comunes por las que alguien podría insertar un símbolo de marca de verificación:

1. **Indicar finalización o éxito**: Se usa comúnmente para marcar una tarea como completada o confirmar que algo se ha hecho con éxito. Por ejemplo, en una lista de tareas, podrías usar una marca para mostrar que una tarea ha sido cumplida.

2. **Listas de verificación y encuestas**: En encuestas, formularios o listas de verificación, un símbolo de marca se usa para indicar opciones seleccionadas o para mostrar que un elemento específico cumple con los criterios requeridos.

3. **Aprobación o validación**: Un símbolo de marca puede indicar aprobación o validación de una acción, decisión o documento. A menudo se usa en un contexto formal o semi formal.

4. **Estética de diseño**: En algunos casos, el símbolo de marca se usa simplemente por su atractivo visual o como parte de un elemento de diseño, como en logotipos, infografías o presentaciones.

5. **Respuesta positiva o correcta**: Se puede usar en materiales educativos para resaltar respuestas correctas o el resultado positivo de algo.

6. **Indicar acuerdo o consentimiento**: Una marca puede representar el acuerdo, consentimiento o reconocimiento de una declaración o condición.


## **Cómo insertar símbolo de marca de verificación en Excel**
Aquí tienes una guía clara sobre cómo insertar un símbolo de marca de verificación (✓ o ✔) en Excel, utilizando varios métodos:

### Usando el menú de símbolos

1. Haz clic en la celda donde deseas la marca.
2. Ve a la pestaña Insertar en la cinta de opciones.
3. Haz clic en Símbolo (extremo derecho).
4. En el cuadro de diálogo Símbolo: Elige Fuente (Wingdings o Segoe UI Symbol), Busca (✔ (código de carácter 252) o ✓ (código de carácter 2713))
5. Haz clic en Insertar, luego en Cerrar.

### Usando atajos de teclado
1. Código Alt (solo Windows): Mantén presionada la tecla Alt y escribe el código usando el teclado numérico: Alt + 0252 (✔) — fuente Wingdings, Alt + 10003 (✓) — Segoe UI Symbol
2. Después de escribir, suelta la tecla Alt para insertar el símbolo.

### Copiar y pegar
Puedes copiar un símbolo de marca de verificación y pegarlo en cualquier celda de Excel: ✓ (U+2713) y ✔ (U+2714). Solo cópialo desde aquí y pégalo directamente en una celda.

### Uso del Formato Condicional con una Fórmula
Puedes crear marcas de verificación automáticas con fórmulas y formato condicional:

1. Ingresa una fórmula como: =IF(A1="sí", "✓", "").
2. Personaliza el tamaño de fuente y la alineación para mejorar la apariencia.

### Insertar con la Función CHAR (Fuente Wingdings)
Si usas Wingdings: =CHAR(252)  →  ✔, Luego cambia la fuente de la celda a Wingdings para que se muestre correctamente.

### Insertar usando Casillas de Verificación de Excel (Opcional)

Para casillas de verificación interactivas:
1. Ve a la pestaña Desarrollador (actívala en Opciones si está oculta).
2. Haz clic en Insertar → Controles de formulario → Casilla de verificación.
3. Posiciona la casilla en la hoja.

## **Cómo Insertar el Símbolo de Marca en Aspose.Cells for .NET**
Para insertar un símbolo de marca (✓) en una celda usando Aspose.Cells for .NET, puedes usar los siguientes métodos para cumplir con los requisitos.

1. Añade el símbolo de marca usando Unicode (U+2713).
2. Añade el símbolo de marca usando la fuente de símbolos (Wingdings 2 o Webdings).
3. Añade el símbolo de marca usando una imagen.
4. Añade el símbolo de marca usando un control de casilla de verificación.
5. Añade el símbolo de marca usando formatos condicionales.
6. Añade el símbolo de marca usando una fórmula.

Aquí tienes un ejemplo básico de cómo insertar un símbolo de marca en una celda en Aspose.Cells for .NET:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-insert-tick-symbol.cs" >}}

## **Resultado de salida**

La siguiente captura de pantalla muestra los símbolos de marca de verificación creados por Aspose.Cells for .NET en el archivo de Excel de salida.
<br>
<img src="tick_result.png" width=70% />

{{< app/cells/assistant language="csharp" >}}
