---
title: 更新されたセルだけでなく、ワークシート全体を検証します
type: docs
weight: 80
url: /ja/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **可能な使用シナリオ**
デフォルトでは、GridWebは更新されたセルのみを検証し、ワークシート全体を検証しません。ただし、GridWebがサーバーにリクエストを投稿する前にクライアント側でワークシート全体を検証したい場合は、acwmain.js内のneedValidateall変数をtrueに設定する必要があります。
## **更新されたセルだけでなく、ワークシート全体を検証します**
次のスクリーンショットは、acwmain.js内のneedValidateall変数を表示しています。これをtrueに設定すると、GridWebは更新されたセルだけでなく、ワークシート全体を検証します。

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)


