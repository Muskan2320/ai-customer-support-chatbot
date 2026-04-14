import json
from langchain.docstore.document import Document

def load_documents(path="iat_data.json"):
    with open(path) as f:
        data = json.load(f)

    docs = []

    # ----------------------------
    # SERVICES (description + details)
    # ----------------------------
    for service in data["services"]:
        content = f"{service['name']}: {service.get('description','')}"
        
        # add details also
        if "details" in service:
            content += " Services include: " + ", ".join(service["details"])
        
        docs.append(Document(
            page_content=content,
            metadata={"type": "service", "name": service["name"]}
        ))

    # ----------------------------
    # ABOUT (FULL)
    # ----------------------------
    about = data["about"]

    docs.append(Document(
        page_content=about["story"],
        metadata={"type": "about_story"}
    ))

    docs.append(Document(
        page_content=about["founder_education"],
        metadata={"type": "founder_education_background"}
    ))

    docs.append(Document(
        page_content=about["mission"],
        metadata={"type": "mission"}
    ))

    docs.append(Document(
        page_content=about["vision"],
        metadata={"type": "vision"}
    ))

    # ----------------------------
    # HOMEPAGE INTRO
    # ----------------------------
    docs.append(Document(
        page_content=data["homepage"]["intro"],
        metadata={"type": "intro"}
    ))

    # ----------------------------
    # WHY US
    # ----------------------------
    docs.append(Document(
        page_content=" ".join(data["homepage"]["why_us"]),
        metadata={"type": "why_us"}
    ))

    docs.append(Document(
        page_content="IAT Networks provides BPO, Digital Marketing, Recruitment, and IT Services.",
        metadata={"type": "service_summary"}
    ))

    # ----------------------------
    # WHY CHOOSE US (description + points)
    # ----------------------------
    why_choose = data["homepage"]["why_choose_us"]

    content = why_choose["description"] + " " + " ".join(why_choose["points"])

    docs.append(Document(
        page_content=content,
        metadata={"type": "why_choose_us"}
    ))

    # ----------------------------
    # CLIENTS
    # ----------------------------
    docs.append(Document(
        page_content="Clients include: " + ", ".join(data["homepage"]["clients"]),
        metadata={"type": "clients"}
    ))

    # ----------------------------
    # PRIVACY POLICY (IMPORTANT)
    # ----------------------------
    privacy = data["privacy_policy"]

    for key, value in privacy.items():
        if isinstance(value, list):
            text = key + ": " + ", ".join(value)
        else:
            text = key + ": " + value

        docs.append(Document(
            page_content=text,
            metadata={"type": "privacy", "section": key}
        ))

    contact = data["contact"]

    docs.append(Document(
        page_content=f"IAT Networks is located at {contact['address']}.",
        metadata={"type": "location_address"}
    ))

    docs.append(Document(
        page_content=f"You can contact IAT Networks via phone at {contact['phone']} or email at {contact['email']}.",
        metadata={"type": "contact"}
    ))

    return docs, data