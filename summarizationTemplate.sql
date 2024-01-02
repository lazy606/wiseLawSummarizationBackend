CREATE TABLE summarization(
    "id",
    "案例类型",
    "案件名称",
    "案号",
    "一审法院",
    "二审法院",
    "再审法院",
    "案情摘要",
    "裁判要点",
    "推荐理由",
    "一审生效文书字号",
    "二审生效文书字号",
    "再审生效文书字号"
);

CREATE TABLE party (
  "id",
  "名称",
  "一审诉讼地位": "",
  "二审诉讼地位": "",
  "再审诉讼地位": "",
  "类型",
  "所属摘要id"
);

CREATE TABLE keyword (
  "id",
  "关键词",
  "所属摘要id",
);

CREATE TABLE argument(
    "id",
    "争议焦点",
    "所属摘要id"
);

CREATE TABLE applicableLaw (
    "id",
    "label",
    "content"
    "所属摘要id"
);