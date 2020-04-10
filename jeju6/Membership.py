class member:
    def __init__ (member, name, age, address, height, weight,is_on_disease):
        member.name = name
        member.age = age
        member.address = address
        member.height = height
        member.weight = weight
        member.is_on_disease = is_on_disease

    def high_risk_group(member):
        if member.weight >= 60:
            return True
        else:
            return False


