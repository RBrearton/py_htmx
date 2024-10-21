"""
This script contains the definition of the BaseModel class. This is the base
class for all the htmx models.
"""

from typing import Annotated, Literal, Self

from pydantic import BaseModel, StringConstraints


class HtmxComponent(BaseModel):
    """
    The base class for all the htmx models.
    """

    id: str | Self = None
    cls: str = None
    style: str | None = None
    accesskey: (
        Annotated[str, StringConstraints(min_length=1, max_length=1)] | None
    ) = None
    contenteditable: bool | None = None
    dir: Literal["ltr", "rtl", "auto"] | None = None
    draggable: bool | None = None
    enterkeyhint: (
        Literal["enter", "done", "go", "next", "previous", "search", "send"]
        | None
    ) = None
    hidden: bool | None = None
    inert: bool | None = None
    inputmode: (
        Literal[
            "none",
            "text",
            "decimal",
            "numeric",
            "tel",
            "search",
            "email",
            "url",
        ]
        | None
    ) = None
    lang: str | None = None
    popover: Literal["auto", "manual", "hover", "focus", "click"] | None = None
    spellcheck: bool | None = None
    tabindex: int | None = None
    translate: bool | None = None
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_delete: str | None = None
    hx_patch: str | None = None
    hx_trigger: str | None = None
    hx_target: str | None = None
    hx_swap: (
        str
        | Literal[
            "innerHTML",
            "outerHTML",
            "afterbegin",
            "beforebegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ]
    ) = None
    hx_swap_oob: (
        str
        | Literal[
            "true",
            "innerHTML",
            "outerHTML",
            "afterbegin",
            "beforebegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ]
    ) = None
    hx_include: str | None = None
    hx_select: str | None = None
    hx_select_oob: str | None = None
    hx_indicator: str | None = None
    hx_push_url: str | Literal["true", "false"] = None
    hx_confirm: str | None = None
    hx_disable: str | None = None
    hx_replace_url: str | Literal["true", "false"] = None
    hx_vals: str | None = None
    hx_disabled_elt: str | Literal["this", "next", "previous"] = None
    hx_ext: str | None = None
    hx_headers: str | None = None
    hx_history: str | Literal["false"] = None
    hx_history_elt: str | None = None
    hx_inherit: str | None = None
    hx_params: str | Literal["*", "none"] = None
    hx_preserve: str | None = None
    hx_prompt: str | None = None
    hx_request: str | None = None
    hx_sync: str | None = None
    hx_validate: Literal["true", "false"] | None = None
