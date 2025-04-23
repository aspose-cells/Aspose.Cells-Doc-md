---
title: ソースコードパッケージからAspose.Cells for Go via C++をビルドする方法。
type: docs
linktitle: ソースコードからビルドする
weight: 50
url: /ja/go-cpp/how-to-build-aspose-cells-for-go-via-c++-from-the-source-code-package
---


## **Aspose.Cells for Go via C++をソースコードパッケージからビルドする方法**

### 1. Aspose.Cells for Go via C++のソースパッケージをダウンロード

- **ソースコードパッケージは次の二つの場所からダウンロードできます：**

1. [Aspose.Cells for Go via C++ダウンロードページ](https://downloads.aspose.com/cells/go-cpp/)からソースコードパッケージをダウンロード  
1. [GitHubリポジトリ](https://github.com/aspose-cells/aspose-cells-go-cpp)からダウンロードするか、または[GitHubアーカイブパッケージ](https://github.com/aspose-cells/aspose-cells-go-cpp/archive/refs/heads/main.zip)を直接取得してください。  

### 2. Aspose.Cells for Go via C++パッケージをプロジェクトにインストールする方法

- **プロジェクト用のディレクトリとmain.goファイルを作成し、次のコードをmain.goに追加してください。**

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

- **go.modを初期化します**

```bash

go mod init main

```

- **ZIPファイルを解凍し、cells-go-cppフォルダに配置します。**

 --cells-go-cppサンプル
   -- cells-go-cpp (フォルダ)
     -- start_up.go
     -- aspose_cells.go
     -- ......
     -- go.mod
     -- AsposeCellsCWrapper.h
   -- main.go
   -- go.mod

- **Goの`mod`ファイルを修正して、パッケージの場所を指定してください。**

   ```go
    module main

    go 1.19

    require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0
    replace github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.1.0  => ./cells-go-cpp
   ```

- **PATHを設定し、現在のコマンドシェル内でAspose.Cells for Go via C++の共有ライブラリを指すようにしてください。`your_version`は実行中のAspose.Cells for Go via C++のバージョンに置き換えます。**

```bash

set PATH=%PATH%;%YourProjectPath%/cells-go-cpp-samples/cells-go-cpp/lib/win_x86_64/

```

またはPowerShellで

```powershell

$env:Path = $env:Path+ ";${YourProjectPath}\cells-go-cpp-samples\cells-go-cpp\lib\win_x86_64\"

```

上記のパスからDLLファイルをコピーして、プロジェクトの実行ファイルと同じ場所に配置することもできます。

- **作成したアプリケーションを実行します。**

```bash

go run main.go

```
