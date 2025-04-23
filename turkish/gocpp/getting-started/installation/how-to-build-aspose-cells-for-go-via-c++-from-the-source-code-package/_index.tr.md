---
title: Aspose.Cells for Go via C++ Cipini kaynak kod paketinden nasıl oluşturulur.
type: docs
linktitle: Kaynak Kodundan Oluşturma
weight: 50
url: /tr/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Aspose.Cells for Go via C++ Cipini kaynak kod paketinden nasıl oluşturulur**

### 1. Aspose.Cells for Go via C++ kaynak paketini indirin

- **Kaynak kod paketini iki konumdan indirebilirsiniz:**

1. Kaynak kod paketini [Aspose.Cells for Go via C++ indirme sayfasından](https://downloads.aspose.com/cells/go-cpp/) indirin.  
1. Kaynak kod paketini [GitHub deposundan](https://github.com/aspose-cells/aspose-cells-go-cpp) veya doğrudan [GitHub Arşiv Paketi](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip) üzerinden indirin.  

### 2. Aspose.Cells for Go via C++ paketini projenize nasıl kurmalısınız

- **Projeniz için bir dizin oluşturun ve içine main.go dosyası ekleyin. main.go'nuza aşağıdaki kodu ekleyin.**

```Go

package main

import (
 . "asposecells"
 "fmt"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String("YOUR_LICENSE_File_PATH")
 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_String_Bool("Hello World!", true)
 style, _ := cell.GetStyle()
 style.SetPattern(BackgroundType_Solid)
 color, _ := NewColor()
 color.Set_Color_R(uint8(255))
 color.Set_Color_G(uint8(128))
 style.SetForegroundColor(color)
 cell.SetStyle_Style(style)
 workbook.Save_String("HELLO.pdf")

}

```

- **Proje go.mod dosyasını başlatın**

```bash

go mod init main

```

- **ZIP dosyasını proje dizininizdeki cells-go-cpp klasörüne çıkarın.**

 --cells-go-cpp-samples
   -- hücreler-go-cpp (klasör)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Go `mod` dosyanızı paket konumunu belirtecek şekilde değiştirin:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Mevcut komut kabuğunuzda PATH'inizi Aspose.Cells for Go via C++ içindeki paylaşılan kütüphanelere işaret edecek şekilde ayarlayın. your_version yerine çalıştırdığınız Aspose.Cells for Go via C++ sürümünü koyun.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Veya PowerShellinizde

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Yukarıdaki dizinden DLL dosyalarını projenizin çalıştırılabilir dosyasıyla aynı yere kopyalayabilirsiniz.

- **Oluşturduğunuz uygulamayı çalıştırın.**

```bash

go run main.go

```
