---
title: Как собрать Aspose.Cells for Go via C++ из пакета исходного кода.
type: docs
linktitle: Сборка из исходного кода
weight: 50
url: /ru/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Как собрать Aspose.Cells for Go via C++ из пакета исходного кода**

### 1. Скачать исходный пакет Aspose.Cells for Go via C++

- **Вы можете скачать исходный пакет двумя способами:**

1. Скачать исходный пакет с [страницы загрузки Aspose.Cells for Go via C++](https://downloads.aspose.com/cells/go-cpp/).  
1. Скачать исходный пакет с [репозитория GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) или напрямую через [архив пакета на GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip).  

### 2. Как установить пакет Aspose.Cells for Go via C++ в ваш проект

- **Создайте каталог для вашего проекта и файл main.go внутри него. Добавьте следующий код в ваш main.go.**

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

- **Инициализировать project go.mod**

```bash

go mod init main

```

- **Распакуйте ZIP-файл в папку cells-go-cpp в каталог вашего проекта.**

 --cells-go-cpp-samples
   -- cells-go-cpp (папка)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Измените ваш файл Go `mod`, чтобы указать расположение пакета:**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **Установите ваш PATH, чтобы указывать на общие библиотеки в Aspose.Cells for Go via C++ в текущей командной оболочке. Замените your_version на версию Aspose.Cells for Go via C++, которую вы используете.**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

Или в PowerShell

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

Вы также можете скопировать файлы DLL из вышеназванного пути в то же место, где находится ваш исполняемый файл проекта.

- **Запустите ваше созданное приложение.**

```bash

go run main.go

```
