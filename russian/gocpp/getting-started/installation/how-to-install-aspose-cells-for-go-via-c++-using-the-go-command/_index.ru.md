---
title: Как установить Aspose.Cells for Go via C++ с помощью команды Go.
type: docs
linktitle: Установка через команду Go
weight: 40
url: /ru/go-cpp/how-to-install-aspose-cells-for-go-via-c++-using-the-go-command
---


## **Как установить Aspose.Cells for Go via C++ с помощью команды Go**

   Начиная с Go 1.16, вы используете команду `go install` для непосредственной установки пакета Aspose.Cells for Go via C++. Эта команда позволяет глобально установить командные инструменты без опасений влиять на существующие зависимости проекта.

```go

go install github.com/aspose-cells/aspose-cells-go-cpp/v25@latest

```

   Когда вы используете команду `go get` для установки пакета Aspose.Cells for Go via C++, в текущем каталоге или любом его родительском должен находиться файл go.mod. см. [установку пакета Aspose.Cells for Go via C++ и запуск вашего кода в вашем проекте](#Installation-in-your-project)

```go

go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1

```

### Установка пакета Aspose.Cells for Go via C++ и запуск вашего кода в вашем проекте {#Installation-in-your-project}

1. Создайте каталог для вашего проекта и файл main.go внутри. Добавьте следующий код в ваш main.go.

```Go

package main

import (
 . "github.com/aspose-cells/aspose-cells-go-cpp/v25"
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

1. Инициализируйте проект go.mod

```bash

go mod init main

```

1. Получите зависимости для вашего проекта.

```bash

go mod tidy

```

Если Aspose.Cells for Go via C++ не установлен в среде разработки, Go автоматически установит пакет в подкаталог `$GOPATH`.

1. Установите переменную PATH, указывающую на общие библиотеки в Aspose.Cells for Go via C++ в вашей текущей командной оболочке. Замените your_version на версию Aspose.Cells for Go via C++, которую вы используете.

```bash

set PATH=%PATH%;%GOPATH%/pkg/mod/github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.1.1/lib/linux_x86_64/

```

Или в PowerShell

```powershell

$env:Path = $env:Path+ ";${env:GOPATH}\github.com\aspose-cells\aspose-cells-go-cpp\v25@v25.1.1\lib\win_x86_64\"

```

Вы также можете скопировать файлы DLL из вышеназванного пути в то же место, где находится ваш исполняемый файл проекта.

1. Запустите созданное вами приложение.

```bash

go run main.go

```
