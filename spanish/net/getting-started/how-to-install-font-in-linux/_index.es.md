---
title: Cómo instalar fuentes en Linux
type: docs
description: "Cómo instalar fuentes en Linux"
weight: 139
url: /es/net/how-to-install-font-in-linux/
---

## Resumen

Cuando uses Aspose.Cells en Linux, como Linux tiene menos fuentes predeterminadas, la fuente referenciada en tu archivo de Excel puede no existir por defecto en tu sistema Linux.
Cuando esto sucede, Aspose.Cells usará una fuente similar para mostrar los caracteres. Sin embargo, esto podría causar los siguientes efectos:

1. Diferentes fuentes pueden resultar en imágenes que se renderizan en diseños diferentes a los de Excel.
2. Dado que la fuente ha cambiado, los caracteres de salida pueden no ser de tu agrado.

Para que tu programa produzca resultados más precisos, instala las fuentes que necesitas en Linux. Es importante asegurarte de que las fuentes que usas en archivos de Excel existan en tu entorno.

## Cómo instalar la fuente en Linux

Hay dos formas de instalar fuentes en Linux, como se describe a continuación:

### Copiar los archivos de fuente en la ruta del sistema Linux

1. Coloca una carpeta llamada "fonts" en el directorio de tu programa, copia los archivos de fuente que necesitas en esta carpeta.
2. Añade el siguiente comando a tu Dockerfile de Linux:
```
COPY fonts/ /usr/share/fonts
```
3. Después de la operación anterior, los archivos de fuente se copiarán en la ruta del sistema Linux. Aspose.Cells irá a la ruta del sistema para encontrarlas y usarlas. Este es nuestro escenario recomendado.

### Configurar carpeta de fuentes con la API de Aspose.Cells
En algunos casos, es posible que no puedas controlar o modificar el directorio del sistema Linux. Por ejemplo, en servidores en la nube. En este caso, puedes usar el segundo escenario.
1. Coloca una carpeta llamada "fonts" en el directorio de tu programa, copia los archivos de fuente que necesitas en esta carpeta.
2. En el código de tu programa, llama a la API de Aspose.Cells:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. La operación anterior garantizará que el programa pueda encontrar la fuente desde la ruta del proyecto.

## Ver También

- [Cómo ejecutar Aspose.Cells para .Net6](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
