---
title: Convertir Excel a archivos PDF en Ruby
type: docs
weight: 30
url: /es/java/converting-excel-to-pdf-files-in-ruby/
---

## **Aspose.Cells - Convertir Excel a archivos PDF**
Para convertir Excel a archivo Pdf usando Aspose.Cells for Java en Ruby, simplemente invoque el método excel_to_pdf() del módulo del Convertidor.

**Código Ruby**

{{< highlight ruby >}}

 def excel_to_pdf(workbook)

    save_format = Rjb::import('com.aspose.cells.SaveFormat')

    # Save the document in PDF format

    workbook.save(@data_dir + "MyPdfFile.pdf", save_format.PDF)

    puts "Pdf saved successfully."

end 

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Convertir Excel a archivos PDF (Aspose.Cells)** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Ruby/lib/asposecellsjava/converter.rb)
