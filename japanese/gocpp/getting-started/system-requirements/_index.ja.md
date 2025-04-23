---
title: システム要件
type: docs
weight: 30
url: /ja/go-cpp/system-requirements/
---

Aspose.Cells for Go via C++は、Office AutomationやMicrosoft Excelアプリケーションを必要とせずに、Go開発者がスプレッドシートをプログラムで作成、操作、変換できるネイティブGoライブラリです。

## サポートされているオペレーティングシステム

Aspose.Cells for Goは以下の64ビットオペレーティングシステムとプラットフォームをサポートしています：

<table>  
 <tr>
   <td style="font-weight: bold; width:400px">オペレーティングシステム</td>
   <td style="font-weight: bold; width:400px">バージョン</td>
  </tr>
  <tr>
   <td>Microsoft Windows</td>
   <!--- <td><ul><li>Windows 2008 Server (x64)</li><li>Windows 2012 Server (x64)</li><li>Windows 2012 R2 Server (x64)</li><li>Windows 2016 Server (x64)</li><li>Windows 2019 Server (x64)</li><li>Windows Vista (x64)</li><li>Windows 7 (x64)</li><li>Windows 8, 8.1 (x64)</li><li>Windows 10 (x64)</li><li>Windows 11 (x64)</li></ul></td> --->
   <td><ul><li>Windows x86_64</li></ul></td>
  </tr>
  <tr>
   <td>Linux</td>
   <td><ul><li>Linux x86_64</li><!---li>Ubuntu 20.04以降</li><li>Fedora</li><li>OpenSUSE</li><li>CentOS</li---></ul></td>
  </tr>
</table>

## 開発環境

Aspose.Cells for Go via C++は、WindowsやLinux用アプリケーションの開発に使用できます。

### Windows

Aspose.Cells for Go via C++は、[Microsoft Visual Studio v142 Platform Toolset](https://docs.microsoft.com/en-us/go/porting/binary-compat-2015-2017?view=msvc-160)をサポートする任意の開発環境でアプリケーションの開発に使用できますが、次の表にリストされている環境のみが明示的にサポートされています。

### Linux

Aspose.Cells for Go via C++は、Go 1.13以上をサポートする開発環境でアプリケーションを開発するのに使用できます。ただし、次のコンパイラとツールは明示的にサポートされています:

<table>  
 <tr>
   <td style="font-weight: bold; width:800px">コンパイラ</td>
  </tr>
  <tr>
   <td><ul><li>GCC 9.4.0以降</li></ul></td>
   </tr>
</table>

### Linux への追加依存関係

Aspose.Cells for Go on Linux depends on <a href="https://www.freedesktop.org/wiki/Software/fontconfig/">fontconfig</a> binaries both dynamic library and tool. Please install it before using:

1. Installing fontconfig on Ubuntu or Debian<br>
`sudo apt install libfontconfig fontconfig`
1. Installing fontconfig on Fedora or CentOs<br>
`sudo yum install fontconfig`
