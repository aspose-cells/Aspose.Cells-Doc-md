---
title: デモのセットアップ
type: docs
weight: 40
url: /ja/jasperreports/demos-setup/
---
{{% alert color="primary" %}}

Aspose.Cells for JasperReports には、アプリケーションから Microsoft Excel ドキュメント形式へのレポートのエクスポートを開始するのに役立つ多数のデモ プロジェクトが含まれています。

Aspose.Cells for JasperReports で提供されるデモは、新しいエクスポーターの使用方法を示すために変更された標準の JasperReports デモです。

{{% /alert %}}

Aspose.Cells for JasperReports デモを実行するには、次の手順を実行します。

1.  JasperReports をダウンロードします (例:<https://sourceforge.net/projects/jasperreports/files/archive/>）。単一の JAR だけでなく、アーカイブされたプロジェクト全体をソース コードとデモと共にダウンロードしてください。
1. アーカイブされたプロジェクトを C:\ などのハードディスク上の場所に解凍します。
1. の \demo フォルダーからすべてのデモ フォルダーをコピーします。**Aspose.Cells.JasperReports.zip**に**\<InstallDir>\demo\samples**、 どこ "\<InstallDir>" は、JasperReports を解凍した場所です。デモ ビルド スクリプトは JasperReports のフォルダー構造に依存しているため、この手順が必要です。それ以外の場合は、ビルド スクリプトを変更する必要があります。
1. コピー**aspose.cells.jasperreports.jar**Aspose.Cells.JasperReports.zip の \lib フォルダから**\<インストールディレクトリ>\lib**.
1.  Ant Build Tool と Ivy Dependency Manager を準備します。**\<インストールディレクトリ>\readme.txt**.
1. 変更する**build.xml**で**\<InstallDir>\demo\samples**、クラスパスに aspose.cells.jasperreports.jar を追加します。
   **\<path id="project-classpath"> ... \<pathelement location="../../lib/aspose.cells.jasperreports.jar"/> </path>**.
1. 現在のディレクトリを次の場所に変更します**\<インストールディレクトリ>\demo\hsqldb**次のコマンドラインを実行します。
   **ant runServer**
1. 現在のディレクトリを Aspose.Cells for JasperReports デモのいずれかに変更します。たとえば、**\<InstallDir>\demo\samples\ac.charts**コマンドラインで次のコマンドを実行します。
   **アリテスト** Aspose XLS エクスポーターを使用してレポート ファイルを生成します。
1. 結果のドキュメントの 1 つを開いて表示します。たとえば、**\<InstallDir>\demo\samples\ac.charts\build\reports\AreaChartReport.xls** Microsoft Excel または別のアプリケーションで。
