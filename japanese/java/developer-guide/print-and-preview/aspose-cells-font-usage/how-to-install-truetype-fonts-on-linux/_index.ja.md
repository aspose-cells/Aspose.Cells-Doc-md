---
title: LinuxにTrueTypeフォントをインストールする方法
type: docs
weight: 20
url: /ja/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

もっともありそうなシナリオは、Aspose.Cellsを使用してスプレッドシートをPDFに変換することです。LinuxなどのWindows以外のオペレーティングシステムでこれを行っている場合、このトピックはAspose.Cellsがスプレッドシートを最も忠実にレンダリングするためにLinuxシステムに"Windowsフォント"または"TrueTypeフォント"をインストールする方法について説明しています。

Aspose.Cellsによって変換されたスプレッドシートが可能な限り元のものに近い形で表示されるようにするためには、Linuxシステムに"Windowsフォント"または"TrueTypeフォント"をインストールする必要があるかもしれません。最も一般的に使用されるTrueTypeフォントは、通常、Linuxディストリビューションにデフォルトでプリインストールされていません。

LinuxシステムにTrueTypeフォントを取得する主な方法には次の2つがあります:

1. Windowsマシンからフォントファイル（.TTFおよび.TTC）をLinuxマシンにコピーする。
1. msttcorefontsなどのTrueTypeフォントパッケージをインストールする。

{{% /alert %}}

## **Windows マシンからフォントをコピーする**

Windows マシンの C:\Windows\Fonts ディレクトリから .TTF および .TTC ファイルを Linux マシンの任意のディレクトリにコピーする簡単で迅速な方法があります。Linux にこれらのフォントをインストールまたは登録する必要はありません。アプリケーション内で FontConfigs.setFontFolder メソッドを使用してフォントの場所を指定するだけです。

{{% alert color="primary" %}}

Microsoft はおそらく誰もが自由に使用できるようにフォントのライセンスを提供していますが、フォントのライセンスについては自分で確認してください。

{{% /alert %}}

## **TrueType フォントパッケージをインストールする**

以下の情報に従って、Fedora および Red Hat Enterprise Linux (RHEL) などの Linux ディストリビューションに Microsoft の最も有名な TrueType フォントをインストールする手順が示されています。

{{% alert color="primary" %}}

おそらく 'root' レベルの権限が必要になるため、'root' としてログインするか、sudo を設定します。

{{% /alert %}}

ターミナルを使用して次のように行います。

1. 次の RPM パッケージがインストールされていることを確認します。
   1. **rpm-build**: インストールされていない場合、次のコマンドを使用して rpm-build パッケージをインストールします。

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: インストールされていない場合、次のコマンドを使用します。

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

以下のコマンドを使用して、SourceForge から最新の msttcorefonts スペックファイルをダウンロードします。

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

以前にダウンロードしたスペックファイルと次のコマンドを使用して RPM ファイルをビルドします。

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

RPM ファイルは次の場所に保存されます: /root/rpmbuild/RPMS/noarch/。次のようにインストールします。

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

変更を有効にするためにマシンを再起動します。

上記の手順に従うと、Microsoft の TTFs パッケージがインストールされます。これには次のフォントファミリーが含まれます:

1. Andale Mono
1. Arial Black/Arial (Bold, Italic, Bold Italic)
1. Comic Sans MS (Bold)
1. Courier New (Bold, Italic, Bold Italic)
1. Georgia (Bold, Italic, Bold Italic)
1. Impact
1. Tahoma
1. Times New Roman (Bold, Italic, Bold Italic)
1. Trebuchet (Bold, Italic, Bold Italic)
1. Verdana (Bold, Italic, Bold Italic)
1. Webdings

{{% alert color="primary" %}}

Ubuntu では、Synaptic パッケージマネージャに移動し、**ttf-mscorefonts-installer** パッケージを検索してインストールします。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
