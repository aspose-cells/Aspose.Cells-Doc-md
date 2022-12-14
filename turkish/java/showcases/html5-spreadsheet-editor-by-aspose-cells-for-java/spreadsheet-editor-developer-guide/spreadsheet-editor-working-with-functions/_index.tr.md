---
title: Hesap Tablosu Düzenleyicisi - İşlevlerle Çalışma
type: docs
weight: 60
url: /tr/java/spreadsheet-editor-working-with-functions/
---
**İçindekiler**

- [Formül çubuğu](#SpreadsheetEditor-WorkingwithFunctions-FormulaBar) 
 - saveFormulaBarContents
- [Bir İşlev Ekle](#SpreadsheetEditor-WorkingwithFunctions-InsertaFunction)
### **Formül çubuğu**
Formül çubuğu, sayfa alanının üstündeki bir metin kutusudur. Geçerli hücrenin formülünü görüntüler ve kullanıcının düzenlemesine izin verir.

**Nasıl çalışır?**

 Bir hücre seçildiğinde, formül çubuğu hücre ile senkronize edilir ve formül görüntülenir. Kullanıcının düzenleme yapmasına izin verilir. Kullanıcı düzenleyip enter tuşuna bastığında, JavaScript işlevi**saveFormulaBarContents** Idam edildi
#### **saveFormulaBarContents**
{{< highlight "java" >}}

 function saveFormulaBarContents() {

    var newContents = PF('formulaBar').jq.val();

    $(sheet_datatable.selectedCell).find('.ui-cell-editor-input input').val(newContents);

    sheet_datatable.saveCell($(sheet_datatable.selectedCell));

    return false;

}

{{< /highlight >}}
### **Bir İşlev Ekle**
Bir işlev veya formül eklemek için:

1. Seçmek için bir hücreye tıklayın.
1.  Tıklamak**İşlev Ekle** üstteki düğme.
1.  adresindeki talimatları izleyin.**İşlev Ekle**diyalog
