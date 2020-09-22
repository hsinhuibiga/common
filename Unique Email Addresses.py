#Unique Email Addresses

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            name, domain = email.split("@")
            name = name.split("+")[0].replace(".", "")
            res.add(name + "@" + domain)
        return len(res)