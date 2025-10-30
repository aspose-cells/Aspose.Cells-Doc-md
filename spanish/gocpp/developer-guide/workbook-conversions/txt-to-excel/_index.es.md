---
title: Convertir CSV, TSV y TXT a Excel con Golang vía C++
linktitle: Convertir CSV, TSV y TXT a Excel
type: docs
weight: 30
url: /es/go-cpp/convert-csv-tsv-and-txt-to-excel/
description: Aprende cómo convertir archivos CSV, TSV y TXT a Excel usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Usando Aspose.Cells for C++, puedes convertir archivos CSV a Excel, OpenOffice, PDF, JSON y muchos otros formatos.

{{% /alert %}}

## **Abriendo Archivos CSV**

Los archivos de valores separados por comas (CSV) contienen registros donde los valores están separados por comas. Los datos se almacenan en forma de tabla donde cada columna está separada por el carácter coma y entrecomillada por el carácter de comillas dobles. Si un valor de campo contiene un carácter de comillas dobles, se escapa con un par de comillas dobles. También puedes usar Microsoft Excel para exportar datos de hojas de cálculo a CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel.go" >}}
## **Abrir archivos CSV y reemplazar caracteres inválidos**

En Excel, cuando se abre un archivo CSV con caracteres especiales, los caracteres se reemplazan automáticamente. Lo mismo lo hace la API Aspose.Cells, como se muestra en el ejemplo de código a continuación.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-1.go" >}}
## **Usando el Analizador Preferido**

No siempre es necesario usar la configuración predeterminada del analizador para abrir archivos CSV. A veces, importar un archivo CSV no produce la salida esperada, por ejemplo, cuando el formato de fecha no es el esperado o los campos vacíos se manejan de manera diferente. Para esto, está disponible **TxtLoadOptions.PreferredParsers** para proporcionar tu propio analizador preferido para analizar diferentes tipos de datos según tus requerimientos. El siguiente código de ejemplo demuestra el uso de un analizador preferido.

Se pueden descargar los archivos fuente de muestra y los archivos de salida de las siguientes conexiones para probar esta función.

[samplePreferredParser.csv](samplePreferredParser.csv)

[outputsamplePreferredParser.xlsx](outputsamplePreferredParser.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-2.go" >}}
### **Abriendo Archivos de Texto con Separador Personalizado**

Los archivos de texto se usan para contener datos de hojas de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-3.go" >}}
### **Abriendo archivos delimitados por tabulación**

Los archivos de valores separados por tabulación (Texto) contienen datos de hojas de cálculo pero sin formato. Los datos están ordenados en filas y columnas como en tablas y hojas de cálculo. Básicamente, un archivo delimitado por tabulación es un tipo especial de archivo de texto plano con una tabulación entre cada columna.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-4.go" >}}
### **Apertura de archivos de Valores Separados por Comas y con pestañas (TSV)**

Los archivos de valores separados por tabulación (TSV) contienen datos de hojas de cálculo pero sin formato. Es lo mismo que un archivo delimitado por tabulación donde los datos están ordenados en filas y columnas como en tablas y hojas de cálculo.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TxtToExcel-5.go" >}}
## **Temas avanzados**
- [Cargar o Importar archivo CSV con fórmulas](/cells/es/cpp/load-or-import-csv-file-with-formulas/)
- [Lectura de archivo CSV con múltiples codificaciones](/cells/es/cpp/reading-csv-file-with-multiple-encodings/)
