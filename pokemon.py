class Pokemon():
    def __init__(self):
        self.moves = set(["Tackle", "Growl", "Pound", "Scratch"])
        self.ability = "idk"
        self.item = "idk"
        self.type = set(["Normal"])

        self.level = 1

        self.base_stats = {"HP":100, "ATK":100, "SPA":100, "DEF":100, "SPD":100, "SPE":100}
        self.ivs = {"HP":100, "ATK":100, "SPA":100, "DEF":100, "SPD":100, "SPE":100}
        self.evs = {"HP":100, "ATK":100, "SPA":100, "DEF":100, "SPD":100, "SPE":100}
        self.nature = "idk"
        self.total_stats = {"HP":100, "ATK":100, "SPA":100, "DEF":100, "SPD":100, "SPE":100, "ACC":100, "EVA":100}

        self.status_nv = "None"
        self.status_v = set([])
        self.stat_stages = {"ATK":1, "SPA":1, "DEF":1, "SPD":1, "SPE":1, "ACC":1, "EVA":1}

        self.current_stats = self.total_stats
        self.hp_percent = 1
        
    def update_current_stat(self, stat_key, stat_val, stage = True):
        if stage:
            if stat_key in ["ACC", "EVA"]:
                base = 3
            else:
                base = 2

            if stat_val > 0:
                self.current_stats[stat_key] = self.total_stats[stat_key] * (base+stat_val)/base
            else:
                self.current_stats[stat_key] = self.total_stats[stat_key] * base/(base+stat_val)
        else:
            self.current_stats[stat_key] = stat_val

    def update_status(self, status, volatile = False):
        if volatile and (status not in self.status_v):
            self.status_v.add(status)
        elif self.status_nv == "None":
            self.status_nv = status
        else:
            return False
        return True
    
    def update_stat_stage(self, stat_key, stage):
        if self.stat_stages[stat_key] == 6 and stage > 0 or self.stat_stages[stat_key] == -6 and stage < 0:
            return False
        else:
            self.stat_stages[stat_key] += stage
            
            self.stat_stages[stat_key] = min(self.stat_stages[stat_key], 6)
            self.stat_stages[stat_key] = max(self.stat_stages[stat_key], -6)
            
            self.update_current_stat(stat_key, self.stat_stages[stat_key], stage=True)            
            return True