---
title: Hesap Tablosu Düzenleyicisi - E-Tablolarla Çalışma
type: docs
weight: 20
url: /tr/java/spreadsheet-editor-working-with-sheets/
---
**İçindekiler**

- [Sayfa Ekle ve Kaldır?](#SpreadsheetEditor-WorkingwithSheets-AddandRemoveSheets?) 
 - WorksheetView.onAddNewSheet
 - WorksheetView.onRemoveActiveSheet
- [Sayfaları Yeniden Adlandır](#SpreadsheetEditor-WorkingwithSheets-RenameSheets) 
 - WorksheetView.setActiveSheet
- [Sayfalar arasında geçiş yap](#SpreadsheetEditor-WorkingwithSheets-SwitchbetweenSheets) 
 - WorksheetView.setActiveSheet
### **Sayfa Ekle ve Kaldır?**
Microsoft Excel, tek bir dosyada birden çok sayfaya izin verir. HTML5 Elektronik Tablo Düzenleyici, kullanıcının sayfa eklemesine ve kaldırmasına izin verir. Sayfalar sekmesinde, açılır bir sayfa listemiz var. Seçilen sayfa, editör tarafından açılan sayfadır.

Yeni bir sayfa eklemek için:

1.  Çevirmek**E-Tablolar sekmesi**.
1. **+** (artı) düğmesine tıklayın.

Yeni bir sayfa eklenecek ve düzenleyici buna geçecektir.

Seçili olan sayfayı kaldırmak için:

1.  Çevirmek**E-Tablolar sekmesi**.
1. **-** (eksi) düğmesine tıklayın.

Halihazırda seçili olan sayfa kaldırılacak ve düzenleyici son seçilen sayfaya geçecektir.

![yapılacaklar:resim_alternatif_Metin](4wgvmu8.png)

**Nasıl çalışır?**

 kullanıcı tıkladığında** +** (artı) ve**-** (eksi) düğmesi tıklandığında, JSF arka uç çekirdeği**Çalışma Sayfası Görünümü** kullanarak olayları işler**WorksheetView.onAddNewSheet** ve**WorksheetView.onRemoveActiveSheet** yöntemleri.
#### **WorksheetView.onAddNewSheet**
{{< highlight "java" >}}

     public void onAddNewSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().add();

                getAsposeWorksheets().setActiveSheetIndex(i);

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("New Worksheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}

#### **WorksheetView.onRemoveActiveSheet**
{{< highlight "java" >}}

     public void onRemoveActiveSheet() {

        if (isLoaded()) {

            try {

                int i = getAsposeWorksheets().getActiveSheetIndex();

                getAsposeWorksheets().removeAt(i);

                if (getAsposeWorksheets().getCount() == 0) {

                    int j = getAsposeWorksheets().add();

                    getAsposeWorksheets().setActiveSheetIndex(j);

                }

                purge();

            } catch (com.aspose.cells.CellsException cx) {

                msg.sendMessage("Could not remove sheet", cx.getMessage());

            }

        }

    }

{{< /highlight >}}
### **Sayfaları Yeniden Adlandır**
Bir sayfayı yeniden adlandırmak için:

1.  Çevirmek**E-Tablolar sekmesi**.
1. Düzenlemek için metin kutusundaki sayfa adına tıklayın.
1. Sayfanın adını değiştirin.
1. Bittiğinde, ENTER tuşuna basın veya kutunun dışında herhangi bir yeri tıklayın.

Sayfa yeniden adlandırılacak.

![yapılacaklar:resim_alternatif_Metin](4wgvmu8.png)

**Nasıl çalışır?**

 Metin kutusu değeri değiştirildiğinde, olay sunucuda JSF arka uç çekirdeği tarafından işlenir.**Çalışma Sayfası Görünümü** yöntem kullanarak**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
### **Sayfalar arasında geçiş yap**
Başka bir sayfaya geçmek için:

1.  Çevirmek**E-Tablolar sekmesi**.
1. Açılır menüden bir sayfa seçin.

Düzenleyici seçilen sayfaya geçiş yapacaktır.

![yapılacaklar:resim_alternatif_Metin](4wgvmu8.png)

**Nasıl çalışır?**

 Açılır seçicinin değeri değiştirildiğinde, olay sunucuda JSF arka uç çekirdeği tarafından işlenir.**Çalışma Sayfası Görünümü** yöntem kullanarak**WorksheetView.setActiveSheet**.
#### **WorksheetView.setActiveSheet**
{{< highlight "java" >}}

     public void setActiveSheet(String name) {

        com.aspose.cells.Worksheet w = getAsposeWorksheets().get(name);

        if (w != null) {

            int i = w.getIndex();

            getAsposeWorksheets().setActiveSheetIndex(i);

        } else {

            getAsposeWorksheet().setName(name);

        }

        purge();

    }

{{< /highlight >}}
