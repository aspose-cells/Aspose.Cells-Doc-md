---
title: Excel de formülleri diğer ifade türlerine nasıl dışa aktarabilirsiniz
linktitle: eksen denklem export et
type: docs
weight: 100
url: /tr/python-java/export-equation/
---

Bazen, iş ihtiyaçlarınızı karşılamak için Excel formüllerini kodlarınızda diğer formatlara aktarmanız gerekebilir, o zaman Aspose.Cell kütüphanesi ihtiyaçlarınızı karşılayabilir. Aşağıdaki içerik, Excel formüllerini diğer formatlara nasıl aktaracağınız konusunda bazı yöntemler tanıtmaktadır, umarım bu yöntemler size yardımcı olur.

Burada, Aspose.Cells for Python via Java kullanarak hedeflerinize ulaşmanıza yardımcı olacak örnek kodlar hazırladık. Ayrıca gerekli örnek dosyalar da sağlanmıştır.

Örnek dosya:[Sample.xlsx](Sample.xlsx)

## Denklemleri LaTeX ifadeleri olarak dışa aktarma

Excel'de denklemleri LaTeX ifadeleri olarak dışa aktarmak istiyorsanız, [toLaTeX()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toLaTeX()) metodunu kullanabilirsiniz. 

Aşağıdaki örnek kod, [toLaTeX()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toLaTeX()) metodunun nasıl kullanılacağını ve oluşturulan sonuçların HTML'ye nasıl yerleştirileceğini gösterir:

### To-LaTeX

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Export-equations-as-LaTeX-expressions.py" >}}

## Denklemleri MathML ifadeleri olarak dışa aktarma

Excel'de denklemleri MathML ifadeleri olarak dışa aktarmak istiyorsanız, [toMathML()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toMathML()) metodunu kullanabilirsiniz. 

Aşağıdaki örnek kod, [toMathML()](https://reference.aspose.com/cells/python-java/asposecells.api/equationnode#toMathML()) metodunun nasıl kullanılacağını ve oluşturulan sonuçların HTML'ye nasıl yerleştirileceğini gösterir:

### To-MathML

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Export-equations-as-MathML-expressions.py" >}}



{{< app/cells/assistant language="csharp" >}}
